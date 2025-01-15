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
            if data["password"] != data["confirm_password"]:
                raise serializers.ValidationError({"password": "Password do not match"})
            return data

        def create(self, validated_data):
            validated_data.pop("confirm_password")  # Remove confirm_password
            user = User.objects.create_superuser(
                username=validated_data["username"],
                email=validated_data["email"],
                first_name=validated_data["first_name"],
                last_name=validated_data["last_name"],
                password=validated_data["password"],
            )
            return user
