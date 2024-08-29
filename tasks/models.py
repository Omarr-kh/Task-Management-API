from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)

    USER_TYPE_CHOICES = [
        ("admin", "admin"),
        ("client", "client"),
    ]

    user_type = models.CharField(max_length=10, choices=USER_TYPE_CHOICES)


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()


class Task(models.Model):
    # each task has to be linked with a user
    # all tasks are deleted if the user is deleted
    user = models.ForeignKey(Profile, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    description = models.TextField()
    status = models.BooleanField(default=False, verbose_name="completed")


class ActivityLog(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    endpoint = models.CharField(max_length=300)
    method = models.CharField(max_length=50)
    timestamp = models.DateTimeField(auto_now_add=True)
