from django.shortcuts import render, redirect
from .forms import UploadFileForm
import os
from django.conf import settings

# Create your views here.

def home(request):
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
