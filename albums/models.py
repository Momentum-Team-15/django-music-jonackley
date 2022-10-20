from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    pass

class Album(models.Model):
    title =  models.CharField(max_length=200)
    artist = models.ForeignKey('Artist', on_delete=models.CASCADE, blank=True, null=True)
    created_at =  models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.title} by {self.artist}"

class Song(models.Model):
    name = models.CharField(max_length=200)
    album = models.ForeignKey('Album', on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.name}"

#ForeignKey represents a O2M relationship
#The One is the field and the Many are from the class it is
#defined on(many=more than one).

class Artist(models.Model):
    name= models.CharField(max_length=200)

    def __str__(self):
        return f"{self.name}"
