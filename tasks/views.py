from django.shortcuts import render
from django.http import JsonResponse

from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import generics
from rest_framework import permissions

from .models import Task, ActivityLog
from .serializers import TaskSerializer, ActivityLogSerializer
from .permissions import IsAuthor, IsAdminUser


class ViewLogs(generics.ListAPIView):
    queryset = ActivityLog.objects.all()
    serializer_class = ActivityLogSerializer
    permission_classes = [IsAdminUser]


class TaskList(generics.ListAPIView):
    # queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Task.objects.filter(user=self.request.user.profile)


class CreateTask(generics.CreateAPIView):
    serializer_class = TaskSerializer
    permission_classes = [permissions.IsAuthenticated]


class UpdateDeleteTask(generics.RetrieveUpdateDestroyAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = [permissions.IsAuthenticated, IsAuthor]


@api_view(["GET"])
def api_home(request):
    data = {"message": "hello, world!"}
    return Response(data)
