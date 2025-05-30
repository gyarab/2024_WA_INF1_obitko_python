from django.shortcuts import render, redirect, get_object_or_404
from .models import Song, Author
from .forms import SongUploadForm, CreateAuthorForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required


# Create your views here.


def index(request): 
    return render(request, "web/index.html")

def songs(request): 
    song_list = Song.objects.all()
    return render(request, "web/songs.html", {
        "song_list": song_list
    })

@login_required
def upload_song(request):
    if request.method == "POST":
        form = SongUploadForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect("songs")  
    
    else:
        form = SongUploadForm()

    return render(request, "web/upload_song.html", {"form": form})

def song_detail(request, slug):
    song = get_object_or_404(Song, slug=slug)
    return render(request, "web/song_detail.html", {
        "song": song 
    })

def authors(request):
    author_list = Author.objects.all()
    return render(request, "web/authors.html", {
        "author_list": author_list
    })

def author_detail(request, slug):
    author = get_object_or_404(Author, slug=slug)
    return render(request, "web/author_detail.html", {
        "author": author
    })

@login_required
def crate_author(request):
    if request.method == "POST":
        form = CreateAuthorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("authors")
    else:
        form = CreateAuthorForm()

    return render(request, "web/create_author.html", {"form": form})

def home(request):
    return render(request, 'home.html')

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'registration/register.html', {'form': form})
