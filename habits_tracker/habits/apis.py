from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import RegularHabitInputSerializer, RegularHabitOutputSerializer
from .services import create_regular_habit
from .selectors import get_habit, delete_habit


class RegularHabitCreateAPIView(APIView):

    def post(self, request):
        serializer = RegularHabitInputSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        create_regular_habit(user, **serializer.validated_data)
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


# class RegularHabitUpdateAPIView(APIView):
#
#     def post
