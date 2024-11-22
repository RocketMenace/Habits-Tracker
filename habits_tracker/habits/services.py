from .models import RelatedHabit, RegularHabit
from .serializers import RegularHabitInputSerializer


def create_regular_habit(serializer: RegularHabitInputSerializer):
    data = serializer.validated_data
    if "related_habit" in data.keys():
        related_habit = RelatedHabit.objects.create(**data["related_habit"])
        data["related_habit"] = related_habit
        regular_habit = RegularHabit.objects.create(**data)
        return regular_habit
    else:
        regular_habit = RegularHabit.objects.create(**data)
        return regular_habit
