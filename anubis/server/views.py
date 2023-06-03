from django.shortcuts import render,redirect
import pymongo
from .models import server_details
from django.http import HttpResponse
from django.conf import settings
from django.core.mail import send_mail
client = pymongo.MongoClient('mongodb+srv://root:UR6dgfcLBXkMlkUW@hackton.u1vq7f7.mongodb.net/')
from app1.views import rms
email_id = ""




db = client['aventus']
collection = db['metadata']


def server_train(request):
    data = server_details.objects.all()
   
    result = collection.find({},{'name':1,'email':1})
    form = [(document['name'],document['email']) for document in result]
    global email_id
    if request.method == "POST":
        email_name = request.POST.get('usernames')
        email_id = email_name
        message = f"Hi request to access your model parametrs"
        email_from = settings.EMAIL_HOST_USER
        recipient_list = [email_name]
        subject = "Paramter"
        send_mail( subject, message, email_from, recipient_list )
        return redirect('paymment_page')
    return render(request, 'server/server.html', {'data': data,"form": form})

def server_index(request):
    
    return render(request,'server/index.html')

   
def insert_data(request):
    if request.method == "POST":
        obj = request.POST.get('id_user')
        documnet = collection.find_one({"id":obj})
        obj = server_details(object_id = obj,client_name = documnet['name'],model_acc="90",model_loss = "80")
        obj.save()
        return redirect('server_train')
    
def client_information(request):
    result = collection.find()
    print(result)
    return render(request,'server/clinet_info.html',{'result':result})

def send_mail_user(request):
    user_name,emial_id = rms()
    print(emial_id)
    return HttpResponse('ok')



