from django.db import models
from django import forms
# Create your models here.
class Task(models.Model):
    task=models.CharField(max_length=100)
    priority=models.IntegerField()
    time=models.DateTimeField()

    def __str__(self):
        return self.task