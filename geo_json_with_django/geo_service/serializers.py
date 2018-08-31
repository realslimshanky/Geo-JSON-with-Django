from rest_framework import serializers
from rest_framework_gis.serializers import GeoModelSerializer

from . import models


class ServiceRegionSerializer(GeoModelSerializer):
    provider = serializers.CharField(source='provider.name', read_only=True)
    currency = serializers.CharField(source='provider.currency', read_only=True)

    def create(self, validated_data):
        provider = self.context['request'].user
        validated_data['provider'] = provider
        return models.ServiceRegion.objects.create(**validated_data)

    class Meta:
        model = models.ServiceRegion
        fields = ['id', 'provider', 'name', 'price', 'currency', 'region_coordinates']
