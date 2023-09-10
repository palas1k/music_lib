from django.shortcuts import render
from rest_framework import status
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet

from .models import Album
from .serializers import AlbumSerializer


class MusicAPIView(APIView):
    serializer_class = AlbumSerializer
    permission_classes = [AllowAny]

    def get(self, request):
        post = Album.objects.all().select_related('singer')
        return Response(AlbumSerializer(post, many= True).data, status=status.HTTP_200_OK)

    def post(self, request):
        post = request.data.get('post')
        serializer = AlbumSerializer(data = post)
        if serializer.is_valid(raise_exception=True):
            post_saved = serializer.save()
        return Response(AlbumSerializer(post_saved, many= True).data, status = status.HTTP_201_CREATED)
