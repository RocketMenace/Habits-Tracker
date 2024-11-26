from django.db.models import ForeignKey

from .models import RegularHabit
from django.db.models import ForeignKey
from rest_framework.permissions import DjangoObjectPermissions


def list_habit(user):
    habits = RegularHabit.objects.prefetch_related("related_habit").filter(user=user)
    return habits


def public_list_habit():
    habits = RegularHabit.objects.prefetch_related("related_habit").filter(public=True)
    return habits


def get_habit(habit_id: int) -> RegularHabit:
    habit = RegularHabit.objects.prefetch_related("related_habit").get(pk=habit_id)
    return habit


# def delete_habit(habit_id: int):
#     RegularHabit.objects.get(pk=habit_id).delete()


def update_habit(habit_id: int, data: dict):
    fields = [
        "place",
        "action",
        "start_time",
        "end_time",
        "public",
        "user",
        "related_habit",
        "frequency",
        "is_enjoyable",
        "award",
    ]
    habit = RegularHabit.objects.prefetch_related("related_habit").get(pk=habit_id)
    model_fields = {field.name: field for field in habit._meta.get_fields()}
    foreign_key_field = dict()
    for field in fields:
        if field not in data:
            continue
        model_field = model_fields.get(field)
        if isinstance(model_field, ForeignKey):
            foreign_key_field[field] = data[field]
            continue
        if getattr(habit, field) != data[field]:
            setattr(habit, field, data[field])
    foreign_key_field.pop("user")
    for field_name, value in foreign_key_field.items():
        related_habit = getattr(habit, field_name)
        related_habit.__dict__.update(**value)
        related_habit.save()
    habit.full_clean()
    habit.save()
