from django.urls import path
from rest_framework.permissions import AllowAny
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from habits_tracker.authentication.apps import AuthenticationConfig

app_name = AuthenticationConfig.name

urlpatterns = [
    path(
        "login/",
        TokenObtainPairView.as_view(permission_classes=[AllowAny]),
        name="login",
    ),
    path("token/refresh", TokenRefreshView.as_view(), name="token_refresh"),
]
