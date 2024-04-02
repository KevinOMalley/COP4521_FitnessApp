from django.db import models
from django.contrib.auth.models import User

class Userhealth(models.Model):
    username = models.OneToOneField(User, on_delete=models.CASCADE, primary_key = True,)
    weight = models.IntegerField()
    height = models.IntegerField()
    goals = models.TextField(null=True)
