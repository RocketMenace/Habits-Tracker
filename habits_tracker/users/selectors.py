from .models import User


def delete_user(user_id):
    User.objects.only("pk").get(pk=user_id).delete()


def list_user():

    users = User.objects.all()
    return users


def get_user(user_id):

    user = User.objects.get(pk=user_id)
    return user


def update_user(user_id, data):

    User.objects.update(**data)
