import json

import factory
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from habits_tracker.habits.models import RegularHabit
from habits_tracker.habits.tests.factories import (
    RelatedHabitFactory,
    RegularHabitFactory,
    UserFactory,
    EnjoyableRegularHabitFactory
)


class RegularHabitTestCase(APITestCase):

    def setUp(self):
        self.related_habit = RelatedHabitFactory()
        self.user = UserFactory()
        self.regular_habit = RegularHabitFactory()
        self.client.force_authenticate(user=self.user)

    def test_regular_habit_create(self):
        url = reverse("api:habits:create")
        initial_regular_habit_count = RegularHabit.objects.count()
        data = factory.build(dict, FACTORY_CLASS=RegularHabitFactory)
        # data["related_habit"] = factory.build(dict, FACTORY_CLASS=RelatedHabitFactory)
        data["start_time"] = data["start_time"].strftime("%Y-%m-%dT%H:%M:%SZ")
        data["end_time"] = data["end_time"].strftime("%Y-%m-%dT%H:%M:%SZ")
        data.pop("user")
        json_data = json.dumps(data, indent=4)
        print(json_data)
        response = self.client.post(url, json_data)
        print(response.data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(RegularHabit.objects.count(), initial_regular_habit_count + 1)
        for attr, expected_value in data.items():
            self.assertEqual(response.data[attr], expected_value)

class EnjoyableRegularHabitTestCase(APITestCase):

    def setUp(self):
        self.user = UserFactory()
        self.habit = EnjoyableRegularHabitFactory()
        self.client.force_authenticate(user=self.user)

    def test_enjoyable_habit_create(self):
        url = reverse("api:habits:create")
        initial_count = RegularHabit.objects.filter(is_enjoyable=True).count()
        data = factory.build(dict, FACTORY_CLASS=EnjoyableRegularHabitFactory)
        data.pop("user")
        data["start_time"] = data["start_time"].strftime("%Y-%m-%dT%H:%M:%SZ")
        data["end_time"] = data["end_time"].strftime("%Y-%m-%dT%H:%M:%SZ")
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(RegularHabit.objects.filter(is_enjoyable=True).count(), initial_count + 1)
        for attr, expected_value in data.items():
            self.assertEqual(response.data[attr], expected_value)

    def test_enjoyable_habit_with_award_create(self):
        url = reverse("api:habits:create")
        data = factory.build(dict, FACTORY_CLASS=EnjoyableRegularHabitFactory)
        data.pop("user")
        data["start_time"] = data["start_time"].strftime("%Y-%m-%dT%H:%M:%SZ")
        data["end_time"] = data["end_time"].strftime("%Y-%m-%dT%H:%M:%SZ")
        data["award"] = "Some award"
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)