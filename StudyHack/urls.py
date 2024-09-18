from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("upload/", views.upload_file, name="upload"),
    path("record/", views.record_audio, name="record"),
    path("notes/", views.notes, name="notes"),
    path("flashcards/", views.flashcards, name="flashcards"),
]