import factory
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from habits_tracker.habits.models import RegularHabit
from habits_tracker.habits.tests.factories import (
    RelatedHabitFactory,
    RegularHabitFactory,
    UserFactory,
    EnjoyableRegularHabitFactory,
    RegularHabitWithAwardFactory,
)


class RegularHabitTestCase(APITestCase):

    def setUp(self):
        self.related_habit = factory.build(dict, FACTORY_CLASS=RelatedHabitFactory)
        self.regular_habit = RegularHabitFactory()
        self.user = UserFactory()
        # self.regular_habit = factory.build(dict, FACTORY_CLASS=RegularHabitFactory)
        self.client.force_authenticate(user=self.regular_habit.user)

    def test_regular_habit_create(self):
        url = reverse("api:habits:create")
        initial_regular_habit_count = RegularHabit.objects.count()
        data = factory.build(dict, FACTORY_CLASS=RegularHabitFactory)
        data["related_habit"] = self.related_habit
        data["related_habit"]["start_time"] = data["related_habit"][
            "start_time"
        ].strftime("%Y-%m-%dT%H:%M:%SZ")
        data["related_habit"]["end_time"] = data["related_habit"]["end_time"].strftime(
            "%Y-%m-%dT%H:%M:%SZ"
        )
        data["start_time"] = data["start_time"].strftime("%Y-%m-%dT%H:%M:%SZ")
        data["end_time"] = data["end_time"].strftime("%Y-%m-%dT%H:%M:%SZ")
        data.pop("user")
        response = self.client.post(url, data, format="json")
        response.data["related_habit"].pop("id")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(RegularHabit.objects.count(), initial_regular_habit_count + 1)
        for attr, expected_value in data.items():
            self.assertEqual(response.data[attr], expected_value)

    def test_regular_habit_list(self):
        url = reverse("api:habits:list")
        habits_count = RegularHabit.objects.count()
        response = self.client.get(url)
        self.assertIsNone(response.data["next"])
        self.assertIsNone(response.data["previous"])
        self.assertEqual(response.data["count"], habits_count)
        self.assertEqual(len(response.data["results"]), habits_count)

    def test_public_regular_habit_list(self):
        url = reverse("api:habits:public_list")
        habits_count = RegularHabit.objects.count()
        response = self.client.get(url)
        self.assertEqual(response.data["count"], habits_count)
        self.assertEqual(len(response.data["results"]), habits_count)

    def test_regular_habit_update(self):
        url = reverse("api:habits:update", args=(self.regular_habit.pk,))
        data = factory.build(dict, FACTORY_CLASS=RegularHabitFactory)
        data["related_habit"] = self.related_habit
        data["related_habit"]["start_time"] = data["related_habit"][
            "start_time"
        ].strftime("%Y-%m-%dT%H:%M:%SZ")
        data["related_habit"]["end_time"] = data["related_habit"]["end_time"].strftime(
            "%Y-%m-%dT%H:%M:%SZ"
        )
        data["start_time"] = data["start_time"].strftime("%Y-%m-%dT%H:%M:%SZ")
        data["end_time"] = data["end_time"].strftime("%Y-%m-%dT%H:%M:%SZ")
        data.pop("user")
        response = self.client.put(url, data, format="json")
        for attr, expected_value in data.items():
            self.assertEqual(response.data[attr], expected_value)

    def test_regular_habit_destroy(self):
        url = reverse("api:habits:delete", args=(self.regular_habit.pk,))
        initial_regular_habit_count = RegularHabit.objects.count()
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(RegularHabit.objects.count(), initial_regular_habit_count - 1)
        self.assertRaises(
            RegularHabit.DoesNotExist,
            RegularHabit.objects.get,
            id=self.regular_habit.id,
        )

    def test_regular_habit_with_award_create(self):
        url = reverse("api:habits:create")
        data = factory.build(dict, FACTORY_CLASS=RegularHabitWithAwardFactory)
        data["related_habit"] = factory.build(dict, FACTORY_CLASS=RelatedHabitFactory)
        data["start_time"] = data["start_time"].strftime("%Y-%m-%dT%H:%M:%SZ")
        data["end_time"] = data["end_time"].strftime("%Y-%m-%dT%H:%M:%SZ")
        response = self.client.post(url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)


class EnjoyableRegularHabitTestCase(APITestCase):

    def setUp(self):
        self.user = UserFactory()
        self.habit = factory.build(dict, FACTORY_CLASS=EnjoyableRegularHabitFactory)
        self.client.force_authenticate(user=self.user)

    def test_enjoyable_habit_create(self):
        url = reverse("api:habits:create")
        initial_count = RegularHabit.objects.filter(is_enjoyable=True).count()
        data = self.habit
        data["start_time"] = data["start_time"].strftime("%Y-%m-%dT%H:%M:%SZ")
        data["end_time"] = data["end_time"].strftime("%Y-%m-%dT%H:%M:%SZ")
        response = self.client.post(url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(
            RegularHabit.objects.filter(is_enjoyable=True).count(), initial_count + 1
        )
        for attr, expected_value in data.items():
            self.assertEqual(response.data[attr], expected_value)

    def test_enjoyable_habit_with_award_create(self):
        url = reverse("api:habits:create")
        data = self.habit
        data["start_time"] = data["start_time"].strftime("%Y-%m-%dT%H:%M:%SZ")
        data["end_time"] = data["end_time"].strftime("%Y-%m-%dT%H:%M:%SZ")
        data["award"] = "Some award"
        response = self.client.post(url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
