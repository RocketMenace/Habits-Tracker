from django.urls import path

from habits_tracker.users.apps import UsersConfig
from .apis import (
    UserCreateAPIView,
    UserDeleteAPIView,
    UserListAPIView,
    UserDetailAPIView,
    UserUpdateAPIView,
)

app_name = UsersConfig.name

urlpatterns = [
    path("register/", UserCreateAPIView.as_view(), name="register"),
    path("<int:user_id>/delete/", UserDeleteAPIView.as_view(), name="delete"),
    path("", UserListAPIView.as_view(), name="list"),
    path("<int:user_id>/", UserDetailAPIView.as_view(), name="detail"),
    path("<int:user_id>/update/", UserUpdateAPIView.as_view(), name="update"),
]
