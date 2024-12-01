from django.utils import timezone
from config.env import env


CELERY_BROKER_URL = env("CELERY_BROKER_URL")
CELERY_RESULT_BACKEND = env("CELERY_RESULT_BACKEND")
CELERY_TIMEZONE = "UTC"
CELERY_TASK_TRACK_STARTED = True
CELERY_TASK_TIME_LIMIT = 30 * 60
CELERY_BEAT_SCHEDULER = "django_celery_beat.schedulers:DatabaseScheduler"


CELERY_BEAT_SCHEDULE = {
    "send_telegram_notification": {
        "task": "habits_tracker.habits.tasks.send_notification",
        "schedule": timezone.timedelta(seconds=1),
        "options": {
            "expires": 15.0,
        },
    },
}
