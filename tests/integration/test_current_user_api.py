# Standard Library
import json

# Third Party Stuff
import pytest
from django.urls import reverse


from .. import factories as f

pytestmark = pytest.mark.django_db


def test_get_current_user_api(client):
    url = reverse('user')
    user = f.create_user(email='test@example.com')

    # should require auth
    response = client.get(url)
    assert response.status_code == 401

    client.login(user)
    response = client.get(url)

    # assert response is None
    assert response.status_code == 200
    expected_keys = [
        'id', 'email', 'name', 'phone_number', 'language', 'currency'
    ]
    assert set(expected_keys).issubset(response.data.keys())
    assert response.data['id'] == str(user.id)


def test_patch_current_user_api(client):
    url = reverse('user')
    user = f.create_user(email='test@example.com', name='test')

    data = {
        'name': 'modified_test',
        'email': 'modified_test@example.com'
    }

    # should require auth
    response = client.json.patch(url, json.dumps(data))
    assert response.status_code == 401

    client.login(user)
    response = client.json.patch(url, json.dumps(data))
    # assert response is None
    assert response.status_code == 200
    expected_keys = [
        'id', 'email', 'name', 'phone_number', 'language', 'currency'
    ]
    assert set(expected_keys).issubset(response.data.keys())

    assert response.data['name'] == 'modified_test'
    assert response.data['email'] == 'modified_test@example.com'
