from django.urls import path 

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("songs/", views.songs, name="songs"), 
    path("upload_song/", views.upload_song, name="upload_song"), 
    path("songs/<slug:slug>/", views.song_detail, name="song_detail"),
    path("authors/", views.authors, name="authors"),
    path("authors/<slug:slug>/", views.author_detail, name="author_detail"), 
    path("create_author/", views.crate_author, name="create_author")
]