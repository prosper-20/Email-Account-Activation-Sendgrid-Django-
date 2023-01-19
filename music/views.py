from django.shortcuts import render
from .models import Album, Song


def home(request):
    all_albums = Album.objects.all()
    all_songs = Song.objects.all()
    context = {
        "albums": all_albums,
        "songs": all_songs
    }
    return render(request, 'home.html', context)
