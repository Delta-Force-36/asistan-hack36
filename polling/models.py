from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class polls(models.Model):
    name1 = models.CharField(max_length=200)
    name2 = models.CharField(max_length=200)
    name3 = models.CharField(max_length=200,blank=True)
    name4 = models.CharField(max_length=200,blank=True)

    vote1 = models.IntegerField(default=0)
    vote2 = models.IntegerField(default=0)
    vote3 = models.IntegerField(default=0,blank=True)
    vote4 = models.IntegerField(default=0,blank=True)

    img1 = models.URLField(blank=True)
    img2 = models.URLField(blank=True)
    img3 = models.URLField(blank=True)
    img4 = models.URLField(blank=True)

    date = models.DateTimeField(auto_now_add=True, blank=True)
    auth = models.ForeignKey(User,on_delete=models.CASCADE)


class my_vote(models.Model):
    votes = models.ForeignKey(polls,on_delete=models.CASCADE)
    auth = models.ForeignKey(User,on_delete=models.CASCADE)