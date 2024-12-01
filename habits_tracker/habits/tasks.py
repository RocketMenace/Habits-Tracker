import requests
from celery import shared_task
from django.utils import timezone

from config.settings.telegram import TELEGRAM_URL, TELEGRAM_BOT_TOKEN
from habits_tracker.habits.models import RegularHabit, RelatedHabit


@shared_task(name="habits_tracker.habits.tasks.send_notification")
def send_notification():
    current_time = timezone.now()
    time_step = current_time + timezone.timedelta(seconds=5)
    daily_habits = RegularHabit.objects.filter(frequency="ежедневно").prefetch_related(
        "related_habit", "user"
    )
    related_daily_habits = RelatedHabit.objects.all()
    for habit in daily_habits:
        if current_time < habit.start_time < time_step:
            message = f"Пора выполнять {habit.action}"
            response = requests.get(
                TELEGRAM_URL
                + TELEGRAM_BOT_TOKEN
                + "/sendMessage?chat_id="
                + habit.user.telegram_id
                + "&parse_mode=Markdown&text="
                + message,
            )
            habit.start_time += timezone.timedelta(days=1)
            habit.end_time += timezone.timedelta(days=1)
    RegularHabit.objects.bulk_update(daily_habits, ["start_time", "end_time"])
    #     if habit.related_habit:
    #         if current_time == habit.related_habit.start_time:
    #             message = f"Пора выполнять {habit.related_habit.action}"
    #             response = requests.get(
    #                 TELEGRAM_URL
    #                 + TELEGRAM_BOT_TOKEN
    #                 + "/sendMessage?chat_id="
    #                 + habit.user.telegram_id
    #                 + "&parse_mode=Markdown&text="
    #                 + message,
    #             )
    #             habit.related_habit.start_time += timezone.timedelta(days=1)
    #             habit.related_habit.end_time += timezone.timedelta(days=1)
    #             habit.related_habit.save()
    # RegularHabit.objects.bulk_update(daily_habits, ["start_time", "end_time"])
    # RelatedHabit.objects.bulk_update(daily_habits, ["start_time", "end_time"])

    # weekly_habits = RelatedHabit.objects.filter(
    #     frequency="еженедельно"
    # ).prefetch_related("related_habit", "user")
    # for habit in weekly_habits:
    #     if current_time == habit.start_time:
    #         message = f"Пора выполнять {habit.action}"
    #         response = requests.get(
    #             TELEGRAM_URL
    #             + TELEGRAM_BOT_TOKEN
    #             + "/sendMessage?chat_id="
    #             + habit.user.telegram_id
    #             + "&parse_mode=Markdown&text="
    #             + message,
    #         )
    #         habit.start_time += timezone.timedelta(days=7)
    #         habit.end_time += timezone.timedelta(days=7)
    #         habit.save()
    #     if habit.related_habit:
    #         if current_time == habit.related_habit.start_time:
    #             message = f"Пора выполнять {habit.related_habit.action}"
    #             response = requests.get(
    #                 TELEGRAM_URL
    #                 + TELEGRAM_BOT_TOKEN
    #                 + "/sendMessage?chat_id="
    #                 + habit.user.telegram_id
    #                 + "&parse_mode=Markdown&text="
    #                 + message,
    #             )
    #             habit.related_habit.start_time += timezone.timedelta(days=7)
    #             habit.related_habit.end_time += timezone.timedelta(days=7)
    #             # habit.save()
    # RegularHabit.objects.bulk_update(weekly_habits, ["start_time", "end_time"])
    # RelatedHabit.objects.bulk_update(weekly_habits, ["start_time", "end_time"])
