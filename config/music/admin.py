from django.contrib import admin

from music.models import Singers, Album, Songs, AlbumSong

admin.site.register(Singers)
admin.site.register(Album)
admin.site.register(Songs)
admin.site.register(AlbumSong)
