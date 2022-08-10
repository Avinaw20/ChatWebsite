from unicodedata import name
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
# class Message(models.Model):
#     message=models.TextField(max_length=100)
#     user=models.OneToOneField(User, on_delete=models.CASCADE)
class Room(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(unique=True)
    # members=models.ManyToManyField(User)
    # messages=models.ForeignKey(Message,on_delete=models.CASCADE)

    def __str__(self):
        return self.name