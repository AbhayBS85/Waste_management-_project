from multiselectfield import MultiSelectField
from django.db import models

# Create your models here.
    
class UserData(models.Model):
    user_id=models.AutoField(primary_key=True)  # Auto-generated user ID
    fullname=models.CharField(max_length=100)
    username=models.CharField(max_length=50, unique=True)
    email=models.EmailField(unique=True)
    password=models.CharField(max_length=128)  # Password field
    address=models.CharField(max_length=255, blank=True, null=True)  # Address field
    phone_number=models.CharField(max_length=15, blank=True, null=True) 

    def __str__(self):
        return f"{self.username} {self.user_id}"

class Biowaste(models.Model):
    waste_id=models.AutoField(primary_key=True)  # Auto-generated primary key
    username=models.CharField(max_length=255)  # Name of the user
    contact_no=models.CharField(max_length=15)  # Phone number of the user
    waste_weight=models.CharField(max_length=50)  # Can store "Enter the weight manually" or "Check on pickup"
    manual_weight=models.DecimalField(max_digits=5,decimal_places=2,null=True,blank=True)  # Manually entered weight
    waste_type=models.CharField(max_length=50)  # Category of waste
    address=models.TextField()  # Address of the user

    def __str__(self):
        return f"{self.waste_id} - {self.username}"
    

class NonBiowaste(models.Model):
    waste_id=models.AutoField(primary_key=True)  # Auto-generated primary key
    username=models.CharField(max_length=255)  # Name of the user
    contact_no=models.CharField(max_length=15)  # Phone number of the user
    waste_weight=models.CharField(max_length=50)  # Can store "Enter the weight manually" or "Check on pickup"
    manual_weight=models.DecimalField(max_digits=5,decimal_places=2,null=True,blank=True)  # Manually entered weight
    waste_type=models.CharField(max_length=50)  # Category of waste
    address=models.TextField()  # Address of the user

    def __str__(self):
        return f"{self.waste_id} - {self.username}"
    

class Hazardouswaste(models.Model):
    waste_id=models.AutoField(primary_key=True)  # Auto-generated primary key
    username=models.CharField(max_length=255)  # Name of the user
    contact_no=models.CharField(max_length=15)  # Phone number of the user
    waste_weight=models.CharField(max_length=50)  # Can store "Enter the weight manually" or "Check on pickup"
    manual_weight=models.DecimalField(max_digits=5,decimal_places=2,null=True,blank=True)  # Manually entered weight
    waste_type=models.CharField(max_length=50)  # Category of waste
    address=models.TextField()  # Address of the user

    def __str__(self):
        return f"{self.waste_id} - {self.username}"