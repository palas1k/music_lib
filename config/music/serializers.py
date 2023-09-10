from rest_framework.relations import StringRelatedField
from rest_framework.serializers import ModelSerializer, CharField

from .models import Album, AlbumSong, Songs, Singers


class SingersSerializer(ModelSerializer):
    class Meta:
        model = Singers
        fields = ('name',)


class AlbumSongSerializer(ModelSerializer):
    class Meta:
        model = AlbumSong
        fields = ('song_position',)


class SongSerializer(ModelSerializer):
    # song_position = AlbumSongSerializer(many=True, source='song')
    song_position = StringRelatedField(many=True, source='song')

    class Meta:
        model = Songs
        fields = ('song_name', 'song_position')


class AlbumSerializer(ModelSerializer):
    song_fields = SongSerializer(many=True, source='song')
    singer = CharField(source='singer.name')
    singer_model = SingersSerializer(source='singer')

    class Meta:
        model = Album
        fields = ('singer_model', 'singer', 'year', 'song_fields')
