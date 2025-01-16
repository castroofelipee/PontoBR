import pytest
from rest_framework.test import APIClient
from django.urls import reverse


@pytest.mark.django_db
def test_user_login_success(create_user):
    client = APIClient()
    user = create_user(
        username="castrinholipe",
        email="castrinho123@mail.com",
        password="senhasegura",
        first_name="Felipe",
        last_name="Castro",
    )
    url = reverse("login")
    data = {
        "email": "castrinho123@gmail.com",
        "password": "senhasegura",
    }
    response = client.post(url, data)
    assert response.status_code == 200
    assert "access" in response.data
    assert "refresh" in response.data


@pytest.mark.django_db
def test_user_login_invalid_credentials(create_user):
    client = APIClient()
    user = create_user(
        username="castrinholipe",
        email="Castro",
        password="senhasegura",
        first_name="Felipe",
        last_name="Castro",
    )
    url = reverse("login")
    data = {
        "email": "castrinho123@mail.com",
        "password": "senha_segura",
    }
    response = client.post(url, data)
    assert response.status_code == 400
    assert response.data == {"non_field_errors": ["Email ou senha errado. Por favor verifique"]}
