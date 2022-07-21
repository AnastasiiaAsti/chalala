from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from PIL import Image


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
    phrase = models.CharField(max_length=300)
    chats = models.ManyToManyField(Chat)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.ImageField(
        upload_to='profile_images/', default='default.webp')

    def __str__(self):
        return f"{self.name}({self.id})"

    def get_absolute_url(self):
        return reverse('profiles_detail', kwargs={'pk': self.id})

    def save(self, *args, **kwargs):
        super().save()

        img = Image.open(self.avatar.path)

        if img.height > 100 or img.width > 100:
            new_img = (100, 100)
            img.thumbnail(new_img)
            img.save(self.avatar.path)


class Message(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    chat = models.ForeignKey(Chat, on_delete=models.CASCADE)
    text = models.CharField(max_length=2000)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.text} on {self.date}"

    class Meta:
        ordering = ['date']
