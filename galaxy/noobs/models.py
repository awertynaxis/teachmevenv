from django.db import models
from django.contrib.auth.models import User
from .managers import BaseFilterManager
# Create your models here.db


class Room(models.Model):
    name = models.CharField(max_length=255)
    archived = models.BooleanField(default=False)

    objects = BaseFilterManager()

    def __str__(self):
        return self.name


class Registrations(models.Model):
    email = models.CharField(max_length=255, unique=True)
    password = models.CharField(max_length=255)
    username = models.CharField(max_length=255)

    def __str__(self):
        return self.username


class Task(models.Model):
    title = models.CharField(max_length=255)
    description = models.CharField(max_length=355)
    date_created = models.DateField()
    date_completed = models.DateField()
    until_date = models.DateField()
    user = models.ForeignKey(to=Registrations, on_delete=models.CASCADE, related_name='tasks')
    completed = models.BooleanField(default=False)

    def __str__(self):
        return self.title


class Tasks(models.Model):
    title = models.CharField(max_length=255)
    description = models.CharField(max_length=355, blank=True)
    date_created = models.DateField(null=True, blank=True)
    date_completed = models.DateField(null=True, blank=True)
    until_date = models.DateField(null=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='tasks')
    completed = models.BooleanField(default=False)

    def __str__(self):
        return self.title