from .models import RelatedHabit, RegularHabit
from .serializers import RegularHabitInputSerializer
import requests
from config.settings.telegram import TELEGRAM_URL, TELEGRAM_BOT_TOKEN


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


def send_telegram_notification(habit, telegram_id):
    message = f"Пора выполнять {habit.action}"
    response = requests.get(
        TELEGRAM_URL
        + TELEGRAM_BOT_TOKEN
        + "/sendMessage?chat_id="
        + habit.user.telegram_id
        + "&parse_mode=Markdown&text="
        + message,
    )
