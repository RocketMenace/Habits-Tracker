from rest_framework import serializers

from .models import User


class UserOutputSerializer(serializers.Serializer):

    id = serializers.CharField()
    email = serializers.EmailField()


class UserInputSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = "__all__"
