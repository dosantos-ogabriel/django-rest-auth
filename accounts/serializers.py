from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

from .models import User


class SignUpSerializer(serializers.ModelSerializer):
    name = serializers.CharField(max_length=255, required=True)

    class Meta:
        model = User
        fields = ["email", "password", "token", "name"]
        read_only_fields = ["token"]
        extra_kwargs = {"password": {"write_only": True}}

    def create(self, validated_data):
        return User.objects.create_user(**validated_data, username=validated_data["email"])


class SignInSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(self, user):
        token = self.get_token(user)
        token["email"] = user.email
        token["name"] = user.name
        return token


class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        read_only_fields = ["email", "name"]
        fields = read_only_fields
