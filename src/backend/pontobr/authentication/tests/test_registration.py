import pytest
from rest_framework.test import APIClient
from django.urls import reverse


# é usado para marcar uma função de teste como requerendo o banco de dados.
@pytest.mark.django_db
def test_user_registration_success():
    client = APIClient()
    url = reverse('register')
    data = {
        "first_name": "Felipe",
        "last_name": "Castro",
    }