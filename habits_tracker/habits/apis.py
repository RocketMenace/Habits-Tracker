from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.pagination import PageNumberPagination

from .models import RegularHabit
from .serializers import RegularHabitInputSerializer, RegularHabitOutputSerializer
from .services import create_regular_habit
from .selectors import get_habit, delete_habit, update_habit, list_habit
from habits_tracker.api.pagination import get_paginated_response


class RegularHabitListAPIView(APIView):

    class Pagination(PageNumberPagination):
        page_size = 5
        page_size_query_param = "page_size"

    def get(self, request):
        habits = list_habit()
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

    def get(self, request, habit_id):
        habit = get_habit(habit_id)
        serializer = RegularHabitOutputSerializer(habit)
        return Response(serializer.data, status=status.HTTP_200_OK)


class RegularHabitDeleteAPIView(APIView):

    def delete(self, request, habit_id):
        delete_habit(habit_id)
        return Response(status=status.HTTP_204_NO_CONTENT)


class RegularHabitUpdateAPIView(APIView):

    def put(self, request, habit_id):
        serializer = RegularHabitInputSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        update_habit(habit_id, serializer.validated_data)
        return Response(status=status.HTTP_200_OK)
