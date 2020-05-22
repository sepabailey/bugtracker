from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone
from django.contrib.auth import get_user_model


class CustomUser(AbstractUser):
    display_name = models.CharField(max_length=50, unique=True)


class Ticket(models.Model):
    #  https://docs.djangoproject.com/en/3.0/ref/models/fields/#choices
    NEW = 'NEW'
    IN_PROGRESS = 'IN PROGRESS'
    DONE = 'DONE'
    INVALID = 'INVALID'
    STATUS_CHOICES = [
        (NEW, 'New'),
        (IN_PROGRESS, 'In Progress'),
        (DONE, 'Done'),
        (INVALID, 'Invalid'),
    ]
    # Peter Marsh helped get the migration to work with unique related_name
    title = models.CharField(max_length=50, unique=True)
    date = models.DateTimeField(default=timezone.now)
    description = models.TextField()
    filed_user = models.ForeignKey(
        # https://stackoverflow.com/questions/25964312/not-null-constraint-failed-after-adding-to-models-py
        # https://stackoverflow.com/questions/4604814/django-model-field-default-to-null
        get_user_model(), related_name='filed_user', on_delete=models.CASCADE, default=None, null=True, blank=True)
    ticket_status = models.CharField(
        max_length=25, choices=STATUS_CHOICES, default=NEW)
    assigned_user = models.ForeignKey(
        get_user_model(), related_name='assigned_user', on_delete=models.CASCADE, default=None, null=True, blank=True)
    completed_user = models.ForeignKey(
        get_user_model(), related_name='completed_user', on_delete=models.CASCADE, default=None, null=True, blank=True)

    def __str__(self):
        return self.title
