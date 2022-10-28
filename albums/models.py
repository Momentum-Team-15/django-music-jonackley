from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    birthday = models.DateField(blank=True, null=True)

class Album(models.Model):
    title =  models.CharField(max_length=200)
    artist = models.ForeignKey('Artist', on_delete=models.CASCADE, blank=True, null=True)
    created_at =  models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    user = models.ForeignKey('User', on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return f"{self.title} by {self.artist}"

#ForeignKey represents a O2M relationship
#The One is the field and the Many are from the class it is
#defined on(many=more than one).

class Artist(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return f"{self.name}"

#lass Favorite(models.Model):
   # album = models.ForeignKey('Album', on_delete=models.CASCADE, blank=True, null=True, related_name="favorites")
   # user = models.ForeignKey('User', on_delete=models.CASCADE, blank=True, null=True, related_name="favorites")
   # created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
#class Playlist(models.Model):
   # user= models.ForeignKey('User', on_delete=models.CASCADE)
    #playlist_name = models.CharField(max_length=200)
   # song = models.ForeignKey('Song', on_delete= models.CASCADE)

    #def __str__(self):
      #  return f"{self.user}"