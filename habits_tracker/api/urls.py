from django.urls import path, include

from habits_tracker.api.apps import ApiConfig

app_name = ApiConfig.name

urlpatterns = [
    path(
        "auth/",
        include("habits_tracker.authentication.urls", namespace="authentication"),
    ),
    path("users/", include("habits_tracker.users.urls", namespace="users")),
    path("habits/", include("habits_tracker.habits.urls", namespace="habits")),
]
