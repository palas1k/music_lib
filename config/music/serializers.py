from rest_framework.relations import PrimaryKeyRelatedField
from rest_framework.serializers import ModelSerializer, CharField

from .models import Songs, Album, Singers


class SingerSerializer(ModelSerializer):

    class Meta:
        model = Singers
        fields = ['name']


class AlbumSerializer(ModelSerializer):

    class Meta:
        model = Album
        fields = ('singer', 'created_data')


class AllSongsSerializer(ModelSerializer):
    album_fields = PrimaryKeyRelatedField(queryset=Album.objects.all(), many=True)

    class Meta:
        model = Songs
        fields = ['album_fields', 'song_name', 'album']
