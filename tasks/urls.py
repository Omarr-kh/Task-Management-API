from django.urls import path
from . import views

urlpatterns = [
    path("", views.api_home, name="home"),
    path("view-logs", views.ViewLogs.as_view(), name="view-logs"),
    path("show-tasks", views.TaskList.as_view(), name="show-tasks"),
    path("create-task", views.CreateTask.as_view(), name="create-tasks"),
    path("tasks/<int:pk>", views.UpdateDeleteTask.as_view(), name="update-delete-task"),
]
