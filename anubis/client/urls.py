
from django.urls import path
from .views import index,upload_images

urlpatterns = [
    path("",index,name="index"),
    path("img/",upload_images,name="imgs")
]