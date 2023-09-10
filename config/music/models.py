from datetime import datetime

from django.db import models
from rest_framework.exceptions import ValidationError


class Singers(models.Model):
    name = models.CharField(max_length=255)

    class Meta:
        verbose_name = 'Исполнитель'
        verbose_name_plural = 'Исполнители'

    def __str__(self):
        return self.name


def year_validator(value):
    if value < 1900 or value > datetime.now().year:
        raise ValidationError(
            ('%(value)s is not a correcrt year!'),
            params={'value': value},
        )


class Album(models.Model):
    album_name = models.CharField(max_length=255)
    singer = models.ForeignKey(Singers, on_delete=models.CASCADE)
    song = models.ManyToManyField('Songs', through='AlbumSong', related_name='song_rname')
    year = models.PositiveIntegerField(validators=[year_validator])

    class Meta:
        verbose_name = 'Альбом'
        verbose_name_plural = 'Альбомы'


class AlbumSong(models.Model):
    album = models.ForeignKey(Album, on_delete=models.CASCADE, related_name='album_rname')
    song = models.ForeignKey('Songs', on_delete=models.CASCADE, related_name='song')
    song_position = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.song_position}"

    class Meta:
        unique_together = ('album', 'song_position')



class Songs(models.Model):
    song_name = models.CharField(max_length=255)

    def __str__(self):
        return self.song_name

    class Meta:
        verbose_name = 'Песня'
        verbose_name_plural = 'Песни'
