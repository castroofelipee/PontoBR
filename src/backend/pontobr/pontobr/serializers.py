from rest_framework import serializers
from django.contrib.auth import get_user_model


User = get_user_model()


class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, min_length=8)
    confirm_password = serializers.CharField(write_only=True, min_length=8)

    class Meta:
        model = User
        fields = [
            "first_name",
            "last_name",
            "email",
            "username",
            "passoword",
            "confirm_password",
        ]

        def validate(self, data):
            if data['password'] != data['confirm_password']:
                raise serializers.ValidationError({'password': 'Password do not match'})
