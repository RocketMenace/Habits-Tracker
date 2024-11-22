from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated, AllowAny

from .serializers import UserInputSerializer, UserOutputSerializer
from .services import create_user
from .selectors import delete_user, list_user, get_user, update_user


class UserListAPIView(APIView):

    permission_classes = [IsAuthenticated]

    def get(self, request):
        users = list_user()
        data = UserOutputSerializer(users, many=True).data
        return Response(status=status.HTTP_200_OK, data=data)


class UserCreateAPIView(APIView):

    permission_classes = [AllowAny]

    def post(self, request):
        serializer = UserInputSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        create_user(**serializer.validated_data)
        return Response(status.HTTP_201_CREATED)


class UserDeleteAPIView(APIView):

    permission_classes = [IsAuthenticated]

    def delete(self, request, user_id):
        delete_user(user_id)
        return Response(status=status.HTTP_204_NO_CONTENT)


class UserDetailAPIView(APIView):

    permission_classes = [IsAuthenticated]

    def get(self, request, user_id):
        user = get_user(user_id)
        serializer = UserOutputSerializer(user)
        return Response(serializer.data, status=status.HTTP_200_OK)


class UserUpdateAPIView(APIView):

    permission_classes = [IsAuthenticated]

    def put(self, request, user_id):

        serializer = UserInputSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        update_user(user_id, serializer.validated_data)
        return Response(status=status.HTTP_200_OK)
