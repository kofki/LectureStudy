from django.shortcuts import render, HttpResponse, redirect
from .forms import File_form
from StudyHack.note_creator import testing_transcript, test

# Create your views here.

def home(request):
    return render(request, "home.html") 

def upload_file(request):
    #if request.method == "POST":
     #   file = File_form(request.POST)
     #   with open("StudyHack/transcript_files_test/lecture1.txt", 'w') as f:
      #      for line in file:
      #          f.write(str(line) + '\n')
      #  return redirect('notes')
    return render(request, "upload.html")

def record_audio(request):
    return render(request, "record.html")

def notes(request):
    return render(request, "notes.html", {'text': test})

def flashcards(request):
    return render(request, "flashcards.html")