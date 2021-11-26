from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class User(AbstractUser):
    fullname = models.CharField(max_length=200, null=True, blank=True)
    email = models.EmailField(unique=True)
    username = models.CharField(max_length=200, unique=True, null=True, blank=True)
    bio = models.TextField(max_length=200, null=True, blank=True)
    avatar = models.ImageField(null=True, default='avatar.svg')

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []


    def __str__(self):
        return str(self.fullname)

class Topic(models.Model):
    name = models.CharField(max_length=200, null=True, blank=True)

    class Meta:
        ordering = ['-name']
        
    def __str__(self):
        return self.name


class Room(models.Model):

    name = models.CharField(max_length=200, null=True, blank=True)
    host = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    topic = models.ForeignKey(Topic, on_delete=models.SET_NULL, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    participants = models.ManyToManyField(User, related_name='participants', blank=True)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-updated']

    def __str__(self):
        return self.name


class Message(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    room = models.ForeignKey(Room, on_delete=models.CASCADE, null=True)
    body = models.TextField(null=True, blank=True)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.body[:50]

