from django.urls import path, include

from habits_tracker.habits.apps import HabitsConfig
from .apis import RegularHabitCreateAPIView

app_name = HabitsConfig.name

urlpatterns = [
    path("create/", RegularHabitCreateAPIView.as_view(), name="create"),
]

# urlpatterns = [
#     path("habits/", include((habits_patterns, "habits")))
# ]
