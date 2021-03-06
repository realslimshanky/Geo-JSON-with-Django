# Third Party Stuff
from rest_framework.routers import DefaultRouter

# Geo JSON with Django Stuff
from geo_json_with_django.base.api.routers import SingletonRouter
from geo_json_with_django.users.api import CurrentUserViewSet
from geo_json_with_django.users.auth.api import AuthViewSet
from geo_json_with_django.geo_service.api import ServiceRegionViewSet

default_router = DefaultRouter(trailing_slash=False)
singleton_router = SingletonRouter(trailing_slash=False)

# Register all the django rest framework viewsets below.
default_router.register('auth', AuthViewSet, base_name='auth')
singleton_router.register('user', CurrentUserViewSet, base_name='user')
default_router.register('service', ServiceRegionViewSet, base_name='service')

# Combine urls from both default and singleton routers and expose as
# 'urlpatterns' which django can pick up from this module.
urlpatterns = default_router.urls + singleton_router.urls
