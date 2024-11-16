from rest_framework import serializers
from habits_tracker.users.models import User
from habits_tracker.users.serializers import (
    UserOutputSerializer,
    UserInputSerializer,
)
from .models import RegularHabit


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

    # user = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())
    # place = serializers.CharField()
    # action = serializers.CharField()
    # start_time = serializers.DateTimeField()
    # end_time = serializers.DateTimeField()
    # public = serializers.BooleanField()
    # award = serializers.CharField()
    # related_habit = RelatedHabitInputSerializer(required=False)
    # frequency = serializers.CharField()
    # is_enjoyable = serializers.BooleanField()

    class Meta:
        model = RegularHabit
        exclude = ["user"]



class RegularHabitOutputSerializer(serializers.Serializer):
    user = UserOutputSerializer()
    place = serializers.CharField()
    action = serializers.CharField()
    start_time = serializers.DateTimeField()
    end_time = serializers.DateTimeField()
    award = serializers.CharField()
    related_habit = RelatedHabitOutputSerializer(required=False)
    frequency = serializers.CharField()
    is_enjoyable = serializers.BooleanField()
