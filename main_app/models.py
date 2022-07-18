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

class Message(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    chat = models.ForeignKey(Chat, on_delete=models.CASCADE)
    text = models.CharField(max_length=2000)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.get_message_display()} on {self.date}"
