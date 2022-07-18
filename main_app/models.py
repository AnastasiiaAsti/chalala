from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Profile(models.Model):
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    phrase = models.CharField(max_length=1000)

    def __str__(self):
        return f"{self.name}({self.id})"