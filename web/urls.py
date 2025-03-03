from django.urls import path 

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("songs/", views.songs, name="songs"), 
    path("upload_song/", views.upload_song, name="upload_song")
]