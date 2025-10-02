from django.db import models
from django.contrib.auth.models import User

class Album(models.Model):
    title = models.CharField(max_length=100)
    artist = models.CharField(max_length=100)
    release_date = models.DateField()
    genre = models.CharField(max_length=50)

    def __str__(self):
        return self.title

class Event(models.Model):
    title = models.CharField(max_length=100)
    date = models.DateTimeField()
    venue = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.title

class UserFavoriteAlbum(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='favorite_albums')
    album = models.ForeignKey(Album, on_delete=models.CASCADE, related_name='favorited_by')

    class Meta:
        unique_together = ('user', 'album')
