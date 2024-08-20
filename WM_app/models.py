from django.db import models

# Create your models here.

class biowaste(models.Model):
     fullname=models.CharField(max_length=100)
     WasteWeight=models.CharField(max_length=100)
     location=models.CharField(max_length=100)

class nonbiowaste(models.Model):
     fullname=models.CharField(max_length=100)
     WasteWeight=models.CharField(max_length=100)
     location=models.CharField(max_length=100)

class hazards(models.Model):
     fullname=models.CharField(max_length=100)
     WasteWeight=models.CharField(max_length=100)
     location=models.CharField(max_length=100)

