from django.contrib.gis.geos import Polygon, Point
from django.contrib.gis.geos.error import GEOSException

from rest_framework import viewsets, mixins
from rest_framework.decorators import action

from geo_json_with_django.base import response
from .models import ServiceRegion
from .serializers import ServiceRegionSerializer
from .permissions import IsProvider


class ServiceRegionViewSet(mixins.ListModelMixin, mixins.CreateModelMixin,
                           mixins.UpdateModelMixin, mixins.RetrieveModelMixin,
                           mixins.DestroyModelMixin, viewsets.GenericViewSet):
    queryset = ServiceRegion.objects.all()
    serializer_class = ServiceRegionSerializer
    permission_classes = (IsProvider,)

    def create(self, request, *args, **kargs):
        if 'region_coordinates' in request.data:
            request.data['region_coordinates'] = self.get_polygon_object(
                request.data['region_coordinates'])
        return self.perform_deserialization(request.data)

    def update(self, request, *args, **kargs):
        instance = self.get_object()
        if 'region_coordinates' in request.data:
            request.data['region_coordinates'] = self.get_polygon_object(
                request.data['region_coordinates'])
        return self.perform_deserialization(instance, request.data)

    def partial_update(self, request, *args, **kargs):
        instance = self.get_object()
        if 'region_coordinates' in request.data:
            request.data['region_coordinates'] = self.get_polygon_object(
                request.data['region_coordinates'])
        return self.perform_deserialization(instance, request.data)

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

    @staticmethod
    def get_polygon_object(coordinates):
        try:
            coordinates = eval(coordinates)
            if type(coordinates) in [list, tuple] and coordinates:
                if coordinates[0] != coordinates[-1]:
                    coordinates.append(coordinates[0])
                return Polygon(coordinates)
            else:
                raise ValueError
        except (SyntaxError, ValueError, TypeError, GEOSException) as e:
                return str(e)

    def perform_deserialization(self, instance, update={}):
        serializer_class = self.get_serializer_class()
        if self.action in ['create']:
            serializer = serializer_class(data=instance, context={'request': self.request})
        elif self.action in ['update']:
            serializer = serializer_class(instance, update)
        elif self.action in ['partial_update']:
            serializer = serializer_class(instance, update, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return response.Ok(serializer.data)
