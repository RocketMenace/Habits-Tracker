from .models import RegularHabit


def get_habit(habit_id):
    habit = RegularHabit.objects.prefetch_related("related_habit").get(pk=habit_id)
    return habit


def delete_habit(habit_id):
    RegularHabit.objects.get(habit_id).delete()
