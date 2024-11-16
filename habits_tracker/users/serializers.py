from rest_framework import serializers


class UserOutputSerializer(serializers.Serializer):

    id = serializers.CharField()
    email = serializers.EmailField()


class UserInputSerializer(serializers.Serializer):

    email = serializers.EmailField()
