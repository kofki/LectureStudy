from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("", views.home, name="home"),
    path("upload/", views.upload_file, name="upload"),
    path('upload-success/', views.upload_file, name='upload_success'),
    path("flashcards/", views.flashcards, name="flashcards"),
    path("notes/", views.notes, name="notes"),
    path("record/", views.record_audio, name="record"),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
