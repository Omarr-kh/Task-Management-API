from django.contrib import admin
from .models import Task, Profile, ActivityLog

admin.site.register(Task)
admin.site.register(Profile)
admin.site.register(ActivityLog)
