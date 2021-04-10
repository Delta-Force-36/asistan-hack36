from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class doubts(models.Model):
    name = models.CharField(max_length=200)

    topic = models.CharField(max_length=200)

    doubt = models.CharField(max_length=200)

    solution = models.CharField(blank=True,max_length=200)

    date = models.DateTimeField(auto_now_add=True, blank=True)