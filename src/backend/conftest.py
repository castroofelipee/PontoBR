"""
ajuda a configurar dispositivos de teste reutilizáveis
"""

import pytest
from django.contrib.auth import get_user_model


@pytest.fixture
def create_user(db):
    def make_user(**kwargs):
        User = get_user_model()
        return User.objects.create_user(**kwargs)

    return make_user
