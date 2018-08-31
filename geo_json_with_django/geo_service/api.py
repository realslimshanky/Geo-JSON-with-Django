from django.contrib.gis.geos import Point

from rest_framework import viewsets, mixins
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from geo_json_with_django.base import response
from .models import ServiceRegion
from .serializers import ServiceRegionSerializer
from .permissions import IsProvider
from .utils import get_polygon_object


class ServiceRegionViewSet(mixins.ListModelMixin, mixins.CreateModelMixin,
                           mixins.UpdateModelMixin, mixins.RetrieveModelMixin,
                           mixins.DestroyModelMixin, viewsets.GenericViewSet):
    queryset = ServiceRegion.objects.all()
    serializer_class = ServiceRegionSerializer
    permission_classes = (IsAuthenticatedOrReadOnly, IsProvider,)

    def create(self, request, *args, **kargs):
        serializer_class = self.get_serializer_class()
        if 'region_coordinates' in request.data:
            request.data['region_coordinates'] = get_polygon_object(
                request.data['region_coordinates'])
        serializer = serializer_class(data=request.data, context={'request': self.request})
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return response.Created(serializer.data)

    def update(self, request, *args, **kargs):
        serializer_class = self.get_serializer_class()
        instance = self.get_object()
        if 'region_coordinates' in request.data:
            request.data['region_coordinates'] = get_polygon_object(
                request.data['region_coordinates'])
        serializer = serializer_class(instance, request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return response.Ok(serializer.data)

    def partial_update(self, request, *args, **kargs):
        serializer_class = self.get_serializer_class()
        instance = self.get_object()
        if 'region_coordinates' in request.data:
            request.data['region_coordinates'] = get_polygon_object(
                request.data['region_coordinates'])
        serializer = serializer_class(instance, request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return response.Ok(serializer.data)

    @action(methods=['POST'], detail=False)
    def search(self, request, *args, **kargs):
        if 'longitude' not in request.data or 'latitude' not in request.data:
            return response.BadRequest({
                "error": "Both 'longitude' and 'latitude' required"
            })
        else:
            if type(request.data['longitude']) != float or type(request.data['latitude']) != float:
                return response.BadRequest({
                    "error": "Both 'longitude' and 'latitude' should be of type float"
                })
            else:
                point_object = Point([request.data['longitude'], request.data['latitude']])
                queryset = self.get_queryset()
                for region in queryset:
                    if not region.is_coordinate_inclusive(point_object):
                        queryset = queryset.exclude(id=region.id)
                serializer = self.get_serializer(queryset, many=True)
                return response.Ok(serializer.data)
