from rest_framework import status
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from habits_tracker.api.pagination import get_paginated_response
from habits_tracker.api.permissions import IsOwner
from .selectors import get_habit, update_habit, list_habit, public_list_habit
from .serializers import RegularHabitInputSerializer, RegularHabitOutputSerializer
from .services import create_regular_habit


class RegularHabitListAPIView(APIView):

    class Pagination(PageNumberPagination):
        page_size = 5
        page_size_query_param = "page_size"

    def get(self, request):
        user = self.request.user
        habits = list_habit(user)
        return get_paginated_response(
            pagination_class=self.Pagination,
            serializer_class=RegularHabitOutputSerializer,
            queryset=habits,
            request=request,
            view=self,
        )


class PublicHabitsListAPIView(APIView):

    class Pagination(PageNumberPagination):
        page_size = 5
        page_size_query_param = "page_size"

    def get(self, request):
        habits = public_list_habit()
        return get_paginated_response(
            pagination_class=self.Pagination,
            serializer_class=RegularHabitOutputSerializer,
            queryset=habits,
            request=request,
            view=self,
        )


class RegularHabitCreateAPIView(APIView):

    def post(self, request):
        context = {"request": self.request}
        serializer = RegularHabitInputSerializer(data=request.data, context=context)
        serializer.is_valid(raise_exception=True)
        create_regular_habit(serializer)
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class RegularHabitDetailAPIView(APIView):

    permission_classes = [IsAuthenticated & IsOwner]

    def get(self, request, habit_id):
        habit = get_habit(habit_id)
        self.check_object_permissions(request, habit)
        serializer = RegularHabitOutputSerializer(habit)
        return Response(serializer.data, status=status.HTTP_200_OK)


class RegularHabitDeleteAPIView(APIView):

    permission_classes = [IsAuthenticated & IsOwner]

    def delete(self, request, habit_id):
        habit = get_habit(habit_id)
        self.check_object_permissions(request, habit)
        habit.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class RegularHabitUpdateAPIView(APIView):

    permission_classes = [IsAuthenticated & IsOwner]

    def put(self, request, habit_id):
        context = {"request": self.request}
        serializer = RegularHabitInputSerializer(data=request.data, context=context)
        serializer.is_valid(raise_exception=True)
        habit = get_habit(habit_id)
        self.check_object_permissions(request, habit)
        update_habit(habit_id, serializer.validated_data)
        return Response(status=status.HTTP_200_OK)
