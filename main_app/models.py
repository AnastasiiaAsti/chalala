from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

class Chat(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.name}({self.id})"

    def get_absolute_url(self):
        return reverse('chats_detail', kwargs={'pk': self.id})
        
# Create your models here.
class Profile(models.Model):
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    phrase = models.CharField(max_length=1000)
    chats = models.ManyToManyField(Chat)

    def __str__(self):
        return f"{self.name}({self.id})"
    
    def get_absolute_url(self):
        return reverse('profiles_detail', kwargs={'pk': self.id})

