from django.db import models
from django.utils.text import slugify
from django.urls import reverse
from django.contrib.auth.models import User

# Create your models here.
class ChatRoom(models.Model):
    name = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.name

    def save(self):
        if not self.slug:
            self.slug = slugify(self.name)

    def get_absolute_url(self):
        return reverse("chat:chatroom", kwargs={"slug": self.slug})
    
class Message(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    room = models.ForeignKey(ChatRoom, on_delete=models.CASCADE)
    text = models.TextField()
    date = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['date']
    
    def __str__(self):
        return self.text