from django.contrib import admin
from django.urls import path,include

from .views import server_index,server_train,insert_data,client_information,send_mail_user

urlpatterns = [
  
    path('server/',server_train,name='server_train'),
    path('server_index/',server_index,name='server_index'),
    path('insert/',insert_data,name="object"),
    path('client_info',client_information,name="cli_info"),
    path('email_send/',send_mail_user,name='mail_send')
 
]