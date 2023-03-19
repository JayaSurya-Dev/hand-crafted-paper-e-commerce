from django.db import models
from django.utils import timezone


class FAQ(models.Model):
    """
    Database model for Frequent Asked Questions
    """
    question = models.CharField(max_length=200, unique=True)
    answer = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=True)

    def __str__(self):
        """Returns question string"""
        return self.question
