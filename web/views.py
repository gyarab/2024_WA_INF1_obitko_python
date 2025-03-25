from django.shortcuts import render, redirect, get_object_or_404
from .models import Song
from .forms import SongUploadForm
# Create your views here.


def index(request): 
    return render(request, "web/index.html")

def songs(request): 
    song_list = Song.objects.all()
    return render(request, "web/songs.html", {
        "song_list": song_list
    })

def upload_song(request):
    if request.method == "POST":
        form = SongUploadForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect("songs")  
    
    else:
        form = SongUploadForm()

    return render(request, "web/upload_song.html", {"form": form})

def song_detail(request, song_id):
    song = Song.objects.get(id=song_id)
    return render(request, "web/song_detail.html", {
        "song": song 
    })