from rest_framework import serializers

from .models import Task, ActivityLog


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ["title", "description", "status"]

    def create(self, validated_data):
        validated_data["user"] = self.context["request"].user.profile
        return super().create(validated_data)


class ActivityLogSerializer(serializers.ModelSerializer):
    username = serializers.SerializerMethodField()
    class Meta:
        model = ActivityLog
        fields = ["id", "username", "endpoint", "method", "timestamp"]

    def get_username(self, instance):
        return instance.user.username
