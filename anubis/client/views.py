from django.shortcuts import render
from django.http import HttpResponse
import numpy as np
from .utils import data_set

# Create your views here.

def index(request):
    context = {"message": "hello world"}
    return render(request, 'index.html', context)


def upload_images(request):
    if request.method == "POST":
        try:
            cnv_img = request.FILES.getlist('cnv')
            tensorf_data = data_set(cnv_img)
            print(tensorf_data)
            context = {"message": "success"}
            return render(request, 'img_upload.html', context=context)
        except Exception as e:
            context = {"message": str(e)}
            return render(request, 'img_upload.html', context=context)
    else:
        return render(request, 'img_upload.html')
