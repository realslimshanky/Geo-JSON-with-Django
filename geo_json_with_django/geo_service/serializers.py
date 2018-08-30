from rest_framework import serializers
from rest_framework_gis.serializers import GeoModelSerializer

from . import models


class ServiceRegionSerializer(GeoModelSerializer):
    provider = serializers.CharField(source='provider.name')

    def create(self, validated_data):
        provider = self.context['request'].user
        validated_data['provider'] = provider
        return models.ServiceRegion.objects.create(**validated_data)

    class Meta:
        model = models.ServiceRegion
        fields = ['id', 'provider', 'name', 'price', 'region_coordinates']
        read_only_fields = ['provider']
