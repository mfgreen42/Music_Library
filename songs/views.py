from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Song
from . serializer import SongSerializer
from rest_framework import status
from django.shortcuts import get_object_or_404

# Create your views here.

@api_view(['GET'])
def song_list(request):
    if request.method == 'GET':
        song_name = request.query_params.get('song_id')
        songs = Song.objects.all()

        if song_name:
            songs = songs.filter(song_id=song_name)
        serializer = SongSerializer(songs, many=True)
        return Response(serializer.data)


@api_view(['GET'])
def song_detail(request, pk):
    songs = get_object_or_404(Song, pk=pk)
    if request.method == 'GET':
        serializer = SongSerializer(songs)
        return Response(serializer.data)