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
        get_user_model(), related_name='filed_user', on_delete=models.CASCADE)
    ticket_status = models.CharField(
        max_length=25, choices=STATUS_CHOICES, default=NEW)
    assigned_user = models.ForeignKey(
        get_user_model(), related_name='assigned_user', on_delete=models.CASCADE)
    completed_user = models.ForeignKey(
        get_user_model(), related_name='completed_user', on_delete=models.CASCADE)
