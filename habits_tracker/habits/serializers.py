from rest_framework import serializers
from habits_tracker.users.models import User
from habits_tracker.users.serializers import (
    UserOutputSerializer,
    UserInputSerializer,
)
from .models import RegularHabit
from .validators import OneChosenFieldValidator, DurationTimeValidator



class RelatedHabitInputSerializer(serializers.Serializer):
    place = serializers.CharField()
    action = serializers.CharField()
    start_time = serializers.DateTimeField()
    end_time = serializers.DateTimeField()
    public = serializers.BooleanField()


class RelatedHabitOutputSerializer(serializers.Serializer):
    place = serializers.CharField()
    action = serializers.CharField()
    start_time = serializers.DateTimeField()
    end_time = serializers.DateTimeField()


class RegularHabitInputSerializer(serializers.ModelSerializer):

    related_habit = RelatedHabitInputSerializer(required=False)
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = RegularHabit
        fields = "__all__"
        validators = [
            OneChosenFieldValidator("related_habit", "is_enjoyable"),
            DurationTimeValidator("start_time", "end_time"),
        ]


class RegularHabitOutputSerializer(serializers.ModelSerializer):

    related_habit = RelatedHabitOutputSerializer(read_only=True)
    user = UserOutputSerializer(read_only=True)

    class Meta:
        model = RegularHabit
        fields = "__all__"
