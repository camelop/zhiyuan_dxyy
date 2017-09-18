from django.db import models
import json

# Create your models here.

class User(models.Model):
    username = models.CharField(max_length=15)
    password = models.CharField(max_length=20)
    point = models.IntegerField(default=0)
    mark = models.IntegerField(default=0)
    participate = models.BooleanField(default=False)
    finish = models.IntegerField(default=0)

    def stat_default():
        return json.dumps([[0, 0, 0],[0, 0, 0],[0, 0, 0],[0, 0, 0],[0, 0, 0],[0, 0, 0],[0, 0, 0],[0, 0, 0],[0, 0, 0],[0, 0, 0]])
    def open_default():
        return json.dumps([0,0,0,0,0,0,0,0,0,0])

    stat = models.TextField(default=stat_default)
    open = models.TextField(default=open_default)

    def __str__(self):
        return self.username

class Problem(models.Model):
    hint1 = models.BooleanField(default=True)
    hint2 = models.BooleanField(default=True)

    def __str__(self):
        return str(self.id)