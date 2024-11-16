from django.urls import path
from .apis import LoginExample

from habits_tracker.authentication.apps import AuthenticationConfig

app_name = AuthenticationConfig.name

urlpatterns = [
    path("login/", LoginExample.as_view(), name="login"),
]
