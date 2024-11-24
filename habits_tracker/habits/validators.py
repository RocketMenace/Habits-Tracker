from datetime import timedelta
from django.utils import timezone

from rest_framework.serializers import ValidationError


class OneChosenFieldValidator:

    def __init__(self, related_habit, award):

        self.related_habit = related_habit
        self.award = award

    def __call__(self, value):
        if value.get(self.related_habit) and value.get(self.award):
            raise ValidationError(
                f"Одновременный выбор {self.related_habit} и {self.award} невозможен."
            )


class DurationTimeValidator:

    def __init__(self, start_time, end_time):
        self.start_time = start_time
        self.end_time = end_time

    def __call__(self, value):
        if value.get(self.end_time) - value.get(self.start_time) > timedelta(minutes=2):
            raise ValidationError("Время выполнения не может быть больше двух минут.")


class RelatedHabitValidator:

    def __init__(self, is_enjoyable):
        self.is_enjoyable = is_enjoyable

    def __call__(self, value):
        if not value.get(self.is_enjoyable):
            raise ValidationError("Связанная привычка должна быть приятной.")


class EnjoyableHabitValidator:

    def __init__(self, award, related_habit, is_enjoyable):
        self.award = award
        self.related_habit = related_habit
        self.is_enjoyable = is_enjoyable

    def __call__(self, value):
        if value.get(self.is_enjoyable) and (
            value.get(self.related_habit) or value.get(self.award)
        ):
            raise ValidationError(
                "У приятной привычки не может быть вознаграждения или связанной привычки."
            )


class FrequencyValidator:

    def __init__(self, start_time):
        self.start_time = start_time

    def __call__(self, value):
        if timezone.now() + timedelta(days=7) < value.get(self.start_time):
            raise ValidationError("Нельзя выполнять привычку реже, чем 1 раз в 7 дней.")
