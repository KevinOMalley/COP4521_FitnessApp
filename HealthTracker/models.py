from django.db import models
from django.contrib.auth.models import AbstractBaseUser

class Userhealth(models.Model):
    username = models.ForeignKey(AbstractBaseUser, on_delete=models.CASCADE)
    weight = models.IntegerField()
    height = models.IntegerField()
    goals = models.TextField(null=True)
