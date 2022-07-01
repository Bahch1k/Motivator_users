from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    pass


class Motivation(models.Model):
    nickname = models.CharField(max_length=64)
    motivation = models.TextField(max_length=200)