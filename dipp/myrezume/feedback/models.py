from django.db import models
from django.contrib.auth.models import User

class Feedback(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    date = models.DateField()

    def __str__(self):
        return self.title
