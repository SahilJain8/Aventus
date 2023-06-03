import numpy as np
from django.shortcuts import render,redirect
from .utils import model_tranning,create_image,predection
import tensorflow as tf
from django.http import HttpResponse,JsonResponse
import cv2
import numpy as np
import PIL
import io
import threading
# Create your views here.

def index(request):
    context = {"message": "hello world"}
    return render(request, 'index.html', context)


async def upload_images(request):
    if request.method == 'POST':
        MildDemented_images = request.FILES.getlist('MildDemented')
        ModerateDemented_images = request.FILES.getlist('ModerateDemented')
        NonDemented_images = request.FILES.getlist('NonDemented')
        VeryMildDemented_images = request.FILES.getlist('VeryMildDemented')
        md_list = create_image(MildDemented_images)
        mod_list = create_image(ModerateDemented_images)
        nd_list = create_image(NonDemented_images)
        vmd_list = create_image(VeryMildDemented_images)
        datset = np.concatenate([md_list,mod_list,nd_list,vmd_list],axis=0)
        labels = [0] * len(MildDemented_images) + [1] * len(ModerateDemented_images) + [2] * len(NonDemented_images) + [
            3] * len(VeryMildDemented_images)
        Alzheimer_dataset = tf.data.Dataset.from_tensor_slices((datset, labels))
        print(Alzheimer_dataset)
        threading.Thread(target=model_tranning,args=(Alzheimer_dataset,)).start()
    

        return redirect('home')
    else:

        return render(request, 'img_upload.html')


def classfication(request):
    if request.method == "POST":
            img = request.FILES['img']
            np_img_pil = PIL.Image.open(io.BytesIO(img.read()))
            np_img = np.array(np_img_pil, dtype=np.float64())
            img = cv2.resize(np_img, (176, 208))
            pre = predection(img)
            print(img)
            return JsonResponse(str(pre))

    return render(request,'classfication.html')