from django.shortcuts import render, HttpResponse, redirect
from StudyHack.note_creator import testing_transcript
from django.shortcuts import render, redirect
from .forms import UploadFileForm
import os
import secrets
import string
from django.conf import settings

# Create your views here.
def generate_secret_key():
    """Generates a secure secret key for Django settings."""
    chars = string.ascii_letters + string.digits + string.punctuation.replace('\'"\\', '')  # Avoid some problematic characters
    secret_key = ''.join(secrets.choice(chars) for _ in range(50))  # 50-character length is Django's recommendation
    print(secret_key)

def home(request):
    generate_secret_key()
    return render(request, "home.html") 

def handle_uploaded_file(f):
    print('recieved the file')
    upload_dir = os.path.join(settings.BASE_DIR, 'uploaded_files')

    if not os.path.exists(upload_dir):
        os.makedirs(upload_dir)

    file_path = os.path.join(upload_dir, f.name)

    with open(file_path, 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)
    # Additional logic goes here


def upload_file(request):
    upload_successful = False
    
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            handle_uploaded_file(request.FILES['file'])
            upload_successful = True 
    else:
        form = UploadFileForm()
    
    return render(request, 'upload.html', {'form': form, 'upload_successful': upload_successful})

def record_audio(request):
    return render(request, "record.html")

def notes(request):
    string = testing_transcript()
    return render(request, "notes.html", {'text': string})    

def flashcards(request):
    return render(request, "flashcards.html")
