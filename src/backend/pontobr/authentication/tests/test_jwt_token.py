import pytest
from rest_framework_simplejwt.tokens import AccessToken
from datetime import timedelta
from django.conf import settings


@pytest.mark.django_db
def test_jwt_token_lifetime(create_user):
    user = create_user(
        username="usuarioteste", email="teste@exemplo.com", password="senhasegura"
    )
    token = AccessToken.for_user(user)
    assert token.lifetime == timedelta(days=5)
