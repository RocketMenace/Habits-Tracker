from django.contrib.auth.hashers import make_password

from .models import User


def create_user(email: str, password: str) -> User:

    password = make_password(password)
    user = User.objects.create(email=email, password=password)
    return user
