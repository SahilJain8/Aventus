from django.db import models

# Create your models here.
class server_details(models.Model):
    object_id = models.CharField(max_length=255)
    client_name = models.CharField(max_length=255)
    model_acc = models.CharField(max_length=255)
    model_loss = models.CharField(max_length=255)
