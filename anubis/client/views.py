from django.shortcuts import render
from django.http import HttpResponse
import numpy as np


# Create your views here.

def index(request):
    context = {"message": "hello world"}
    return render(request, 'index.html', context)


def upload_images(request):
    if request.method == "POST":
        try:
            cnv_img = np.array(request.FILES.get('cnv').read())
            cnv_img_label = int(len(cnv_img))
            context = {"message": "success"}
            return render(request, 'img_upload.html', context=context)
        except Exception as e:
            context = {"message": str(e)}
            return render(request, 'img_upload.html', context=context)
    else:
        return render(request, 'img_upload.html')
