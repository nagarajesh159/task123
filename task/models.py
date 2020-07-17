from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Task(models.Model):

    status_choices = (
        ('Not started', 'Not started'),
        ('InProgress', "InProgress"),
        ('Done', 'Done'),
    )
    name = models.CharField(max_length=50, unique=True)
    status = models.CharField(max_length=20, choices=status_choices, default='Not started')

    def __str__(self):
        return self.name


class Employee(models.Model):

    designation_choices = (
        ('TL', 'Team Lead'),
        ('employee', "employee"),
    )
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=50, unique=True)
    designation = models.CharField(max_length=10, choices=designation_choices)
    task = models.ForeignKey(Task, on_delete=models.DO_NOTHING, null=True, blank=True)

    def __str__(self):
        return self.name