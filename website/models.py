from django.db import models
from django.contrib.auth.models import User

class Album(models.Model):
    """
    Represents a music album.

    Attributes:
        title (str): The title of the album.
        artist (str): The name of the artist.
        release_date (date): The release date of the album.
        genre (str): The genre of the album.
    """

    title = models.CharField(max_length=100)
    artist = models.CharField(max_length=100)
    release_date = models.DateField()
    genre = models.CharField(max_length=50)

    def __str__(self):
        """
        Returns the album title as its string representation.

        Returns:
            str: The title of the album.
        """
        return self.title


class Event(models.Model):
    """
    Represents a musical event.

    Attributes:
        title (str): The title of the event.
        date (datetime): The date and time of the event.
        venue (str): The venue where the event is held.
        description (str): A description of the event.
    """

    title = models.CharField(max_length=100)
    date = models.DateTimeField()
    venue = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        """
        Returns the event title as its string representation.

        Returns:
            str: The title of the event.
        """
        return self.title


class UserFavoriteAlbum(models.Model):
    """
    Represents a user's favorite album relationship.

    Attributes:
        user (User): The user who favorited the album.
        album (Album): The album that is favorited by the user.

    Meta:
        unique_together: Ensures a user cannot favorite the same album more than once.
    """

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='favorite_albums')
    album = models.ForeignKey(Album, on_delete=models.CASCADE, related_name='favorited_by')

    class Meta:
        unique_together = ('user', 'album')
