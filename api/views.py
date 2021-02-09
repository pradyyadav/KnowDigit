from django.shortcuts import render
from django.http import HttpResponse
from requests import request
from django import forms
from django.core.files.storage import FileSystemStorage
from dl.digit_detection import digit_detection
import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

def index(request):
    print(request.method)
    if request.method == "POST":
        fileName = request.FILES['filename']
        fs = FileSystemStorage()
        if os.path.exists('media/media.png'):
            os.remove('media/media.png') 
        file = fs.save('media/media.png', fileName)
        fileurl = fs.url(file)
        print(fileurl)
        predi = digit_detection(str(BASE_DIR)+ '/media/media.png')
        return render(request,'index.html',{'prediction' : predi})
    return render(request,'index.html')

