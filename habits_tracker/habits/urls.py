from django.urls import path

from habits_tracker.habits.apps import HabitsConfig
from .apis import (
    RegularHabitCreateAPIView,
    RegularHabitDetailAPIView,
    RegularHabitDeleteAPIView,
    RegularHabitUpdateAPIView,
    RegularHabitListAPIView,
    PublicHabitsListAPIView,
)

app_name = HabitsConfig.name

urlpatterns = [
    path("", RegularHabitListAPIView.as_view(), name="list"),
    path("public/", PublicHabitsListAPIView.as_view(), name="public_list"),
    path("create/", RegularHabitCreateAPIView.as_view(), name="create"),
    path("<int:habit_id>/", RegularHabitDetailAPIView.as_view(), name="detail"),
    path("<int:habit_id>/delete/", RegularHabitDeleteAPIView.as_view(), name="delete"),
    path("<int:habit_id>/update/", RegularHabitUpdateAPIView.as_view(), name="update"),
]
