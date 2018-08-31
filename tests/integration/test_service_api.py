# Standard Library
import json

# Django Stuff
from django.contrib.gis.geos import Polygon, Point

# Third Party Stuff
import pytest
from django.urls import reverse

from .. import factories as f

pytestmark = pytest.mark.django_db


def test_list_service_regions(client):
    url = reverse('service-list')
    response = client.get(url)
    assert response.status_code == 200


def test_create_service_region(client):
    url = reverse('service-list')
    user = f.create_user(email='test@example.com', password='newpass.123')

    response = client.post(url)
    assert response.status_code == 401

    client.login(user)
    data = {
        "name": 'Temporary Region',
        "price": 1000,
        "region_coordinates": "[(11.22, 13.11), (22.33, 22.33), (41.11, 42.22), (52.43, 5.22)]"
    }
    response = client.json.post(url, json.dumps(data))
    assert response.status_code == 201


def test_retrieve_service_region(client):
    url = reverse('service-list')
    user = f.create_user(email='test@example.com', password='newpass.123')

    client.login(user)
    data = {
        "name": 'Temporary Region',
        "price": 1000,
        "region_coordinates": "[(11.22, 13.11), (22.33, 22.33), (41.11, 42.22), (52.43, 5.22)]"
    }
    response = client.json.post(url, json.dumps(data))
    url = reverse('service-detail', kwargs={'pk': response.data['id']})
    response = client.get(url)

    assert response.status_code == 200
    expected_keys = [
        'id', 'provider', 'name', 'price', 'currency', 'region_coordinates'
    ]
    assert set(expected_keys).issubset(response.data.keys())


def test_update_service_region(client):
    url = reverse('service-list')
    user = f.create_user(email='test@example.com', password='newpass.123')

    client.login(user)
    data = {
        "name": 'Temporary Region',
        "price": 1000,
        "region_coordinates": "[(11.22, 13.11), (22.33, 22.33), (41.11, 42.22), (52.43, 5.22)]"
    }
    response = client.json.post(url, json.dumps(data))

    # PUT test for full update
    url = reverse('service-detail', kwargs={'pk': response.data['id']})
    updated_data = {
        "name": 'Semi-Permanent Region',
        "price": 1050,
        "region_coordinates": "[(12.00, 13.11), (22.33, 22.33), (41.11, 42.22), (52.43, 5.22)]"
    }
    response = client.json.put(url, json.dumps(updated_data))

    assert response.status_code == 200

    # PATCH test for partial update
    url = reverse('service-detail', kwargs={'pk': response.data['id']})
    updated_data = {"name": 'Permanent Region'}
    response = client.json.patch(url, json.dumps(updated_data))

    assert response.status_code == 200


def test_delete_service_region(client):
    url = reverse('service-list')
    user = f.create_user(email='test@example.com', password='newpass.123')

    client.login(user)
    data = {
        "name": 'Temporary Region',
        "price": 1000,
        "region_coordinates": "[(11.22, 13.11), (22.33, 22.33), (41.11, 42.22), (52.43, 5.22)]"
    }
    response = client.json.post(url, json.dumps(data))
    url = reverse('service-detail', kwargs={'pk': response.data['id']})
    response = client.delete(url)

    assert response.status_code == 204


def test_search_service_region(client):
    url = reverse('service-list')
    user = f.create_user(email='test@example.com', password='newpass.123')

    client.login(user)
    data = {
        "name": 'Temporary Region',
        "price": 1000,
        "region_coordinates": "[(11.22, 13.11), (22.33, 22.33), (41.11, 42.22), (52.43, 5.22)]"
    }
    client.json.post(url, json.dumps(data))

    url = reverse('service-search')
    data = {
        "longitude": 20.00,
        "latitude": 20.00
    }
    response = client.json.post(url, json.dumps(data))

    assert response.status_code == 200
    assert len(response.data) >= 1
