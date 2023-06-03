
from django.urls import path
from .views import index,upload_images,classfication

urlpatterns = [
    path("index/",index,name="home"),
    path("img/",upload_images,name="imgs"),
    path("classfication/",classfication,name="classfication")
]