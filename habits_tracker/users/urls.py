from django.urls import path

from habits_tracker.users.apps import UsersConfig
from .apis import UserCreateAPIView

app_name = UsersConfig.name

urlpatterns = [
    path("register/", UserCreateAPIView.as_view(), name="register"),
]
