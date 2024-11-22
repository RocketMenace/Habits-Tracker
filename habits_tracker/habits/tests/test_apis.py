from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse
from habits_tracker.habits.models import RegularHabit, RelatedHabit


class RegularHabitTestCase(APITestCase):

    def setUp(self):
        pass
