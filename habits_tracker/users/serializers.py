from rest_framework import serializers

from .models import User


class UserOutputSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = "__all__"


class UserInputSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = "__all__"
