from celery import shared_task
from django.db.models import Q, F
from django.utils import timezone

from habits_tracker.habits.models import RegularHabit, RelatedHabit
from habits_tracker.habits.services import send_telegram_notification


@shared_task(name="habits_tracker.habits.tasks.send_notification")
def send_notification():
    current_time = timezone.now()
    time_step = current_time + timezone.timedelta(seconds=5)

    daily_habits = RegularHabit.objects.filter(
        Q(start_time__gt=current_time) & Q(start_time__lt=time_step),
        frequency="ежедневно",
    ).prefetch_related("user")
    related_daily_habits = RelatedHabit.objects.filter(
        Q(start_time__gt=current_time) & Q(start_time__lt=time_step),
        frequency="ежедневно",
    )

    for habit in daily_habits:
        send_telegram_notification(habit, telegram_id=habit.user.telegram_id)
        habit.start_time += timezone.timedelta(days=1)
        habit.end_time += timezone.timedelta(days=1)
    RegularHabit.objects.bulk_update(daily_habits, ["start_time", "end_time"])

    for related_habit in related_daily_habits:
        send_telegram_notification(
            related_habit, telegram_id=related_habit.user.telegram_id
        )
        related_habit.start_time += timezone.timedelta(days=1)
        related_habit.end_time += timezone.timedelta(days=1)
    RelatedHabit.objects.bulk_update(related_daily_habits, ["start_time", "end_time"])

    weekly_habits = RegularHabit.objects.filter(
        Q(start_time__gt=current_time) & Q(start_time__lt=time_step),
        frequency="еженедельно",
    ).prefetch_related("user", "related_habit")
    related_habits_weekly = RelatedHabit.objects.filter(
        Q(start_time__gt=current_time) & Q(start_time__lt=time_step),
        frequency="еженедельно",
    )

    for habit in weekly_habits:
        send_telegram_notification(habit, telegram_id=habit.user.telegram_id)
        habit.start_time += timezone.timedelta(days=7)
        habit.end_time += timezone.timedelta(days=7)
    RegularHabit.objects.bulk_update(weekly_habits, ["start_time", "end_time"])

    for related_habit in related_habits_weekly:
        send_telegram_notification(habit, telegram_id=related_habit.user.telegram_id)
        related_habit.start_time += timezone.timedelta(days=7)
        related_habit.end_time += timezone.timedelta(days=7)
    RelatedHabit.objects.bulk_update(weekly_habits, ["start_time", "end_time"])
