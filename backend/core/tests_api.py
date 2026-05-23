import pytest
from django.urls import reverse
from rest_framework.test import APIClient
from core.models import User

@pytest.fixture
def api_client():
    return APIClient()

@pytest.mark.django_db
def test_user_registration(api_client):
    url = reverse('user-list')
    data = {
        'username': 'testmother',
        'password': 'testpassword123',
        'email': 'mother@example.com',
        'role': 'MOTHER'
    }
    response = api_client.post(url, data)
    assert response.status_code == 201
    assert User.objects.count() == 1

@pytest.mark.django_db
def test_login_and_access_mothers(api_client):
    user = User.objects.create_user(username='mother1', password='password123', role='MOTHER')

    # Get Token
    token_url = reverse('token_obtain_pair')
    response = api_client.post(token_url, {'username': 'mother1', 'password': 'password123'})
    assert response.status_code == 200
    access_token = response.data['access']

    # Access Mothers API
    api_client.credentials(HTTP_AUTHORIZATION=f'Bearer {access_token}')
    mothers_url = reverse('mother-list')
    response = api_client.get(mothers_url)
    assert response.status_code == 200
