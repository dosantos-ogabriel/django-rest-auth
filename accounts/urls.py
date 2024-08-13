from django.urls import path

from . import views

app_name = "accounts"

urlpatterns = [
    path("", views.AccountAPIView.as_view(), name="account"),
    path("signin/", views.SignInAPIView.as_view(), name="signin"),
    path("signup/", views.SignUpAPIView.as_view(), name="signup"),
]
