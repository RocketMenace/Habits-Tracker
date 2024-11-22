from datetime import timedelta
from time import strptime

from rest_framework.serializers import ValidationError


class OneChosenFieldValidator:

    def __init__(self, related_habit, is_enjoyable):

        self.related_habit = related_habit
        self.is_enjoyable = is_enjoyable

    def __call__(self, is_enjoyable):
        if self.related_habit and self.is_enjoyable:
            raise ValidationError(
                f"Одновременный выбор {self.related_habit} и {self.is_enjoyable} невозможен."
            )


class DurationTimeValidator:

    def __init__(self, start_time, end_time):
        self.start_time = start_time
        self.end_time = end_time

    def __call__(self, end_time):
        print(end_time)
        if end_time - self.start_time > timedelta(minutes=2):
            raise ValidationError("Время выполнения не может быть больше двух минут.")
