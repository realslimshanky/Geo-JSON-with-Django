# Third Party Stuff
from rest_framework import viewsets
from rest_framework.decorators import action

# Geo JSON with Django Stuff
from geo_json_with_django.base import response

from . import models, serializers


class CurrentUserViewSet(viewsets.GenericViewSet):
    serializer_class = serializers.UserSerializer
    queryset = models.User.objects.filter(is_active=True)

    def get_object(self):
        return self.request.user

    def list(self, request):
        """Get logged in user profile"""
        serializer = self.get_serializer(self.get_object())
        return response.Ok(serializer.data)

    def partial_update(self, request):
        """Update logged in user profile"""
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return response.Ok(serializer.data)

    def destroy(self, request):
        """Deleting current user"""
        request.user.delete()
        return response.NoContent()

    @action(detail=False)
    def all(self, request):
        """Listing all the active users"""
        serializer = self.get_serializer(self.queryset, many=True)
        return response.Ok(serializer.data)
