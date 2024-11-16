from django.core.management import BaseCommand
from habits_tracker.users.models import User


class Command(BaseCommand):

    def handle(self, *args, **options):
        user = User.objects.create(
            email="djangoadmin@sky.pro",
            first_name="admin",
            last_name="django",
            is_staff=True,
            is_superuser=True,
        )

        user.set_password("123")
        user.save()
