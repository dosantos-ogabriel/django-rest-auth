from django.contrib.auth.models import AbstractUser
from django.db import models
from rest_framework_simplejwt.tokens import RefreshToken


class User(AbstractUser):
    email = models.EmailField(unique=True, blank=False, null=False)

    def __str__(self):
        return self.email

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    @property
    def refresh_token(self) -> str:
        return RefreshToken.for_user(self)

    @property
    def token(self) -> str:
        return str(self.refresh_token.access_token)

    @property
    def refresh(self) -> str:
        return str(self.refresh_token)
