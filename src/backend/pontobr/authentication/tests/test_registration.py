import pytest
from rest_framework.test import APIClient
from django.urls import reverse


# é usado para marcar uma função de teste como requerendo o banco de dados.
@pytest.mark.django_db
def test_user_registration_success():
    client = APIClient()
    url = reverse("register")
    data = {
        "first_name": "Felipe",
        "last_name": "Castro",
        "username": "castrinholipe",
        "email": "castrinho123@mail.com",
        "password": "senhasegura",
        "confirm_password": "senhasegura",
    }
    response = client.post(url, data)
    assert response.status_code == 201
    assert response.data["message"] == "Usuário criado com sucesso"


@pytest.mark.django_db
def test_user_registration_password_mismatch():
    client = APIClient()
    url = reverse("register")
    data = {
        "first_name": "Felipe",
        "last_name": "Castro",
        "username": "castrinholipe",
        "email": "castrinho123@mail.com",
        "password": "senhasegura",
        "confirm_password": "senha_segura",
    }
    response = client.post(url, data)
    assert response.status_code == 400
    assert 'password' in response.data