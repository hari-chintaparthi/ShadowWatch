from django.db import models

# Create your models here.
from django.db.models import CASCADE


class ClientRegister_Model(models.Model):

    username = models.CharField(max_length=30)
    email = models.EmailField(max_length=30)
    password = models.CharField(max_length=10)
    phoneno = models.CharField(max_length=10)
    country = models.CharField(max_length=30)
    state = models.CharField(max_length=30)
    city = models.CharField(max_length=30)
    address= models.CharField(max_length=255, null=True, blank=True, default='N/A')
    gender= models.CharField(max_length=30,null=True, blank=True)

class detection_type(models.Model):

    url=models.CharField(max_length=300)
    length_url=models.CharField(max_length=300)
    length_hostname=models.CharField(max_length=300)
    https_token=models.CharField(max_length=300)
    page_rank=models.CharField(max_length=300)
    Prediction=models.CharField(max_length=300)

class detection_accuracy(models.Model):

    names = models.CharField(max_length=300)
    ratio = models.CharField(max_length=300)

class detection_ratio(models.Model):

    names = models.CharField(max_length=300)
    ratio = models.CharField(max_length=300)



