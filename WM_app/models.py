from multiselectfield import MultiSelectField
from django.contrib.auth.models import User
from django.utils import timezone
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
    

class Pickup(models.Model):
    pickup_id=models.AutoField(primary_key=True)
    customer=models.CharField(max_length=255)
    contact_number=models.CharField(max_length=15)  
    waste_type=models.CharField(max_length=50)
    weight=models.CharField(max_length=50)
    location=models.TextField()
    payment_status=models.CharField(max_length=50)
    date=models.DateTimeField(default=timezone.now)  
    pickup_status=models.CharField(max_length=50,default='Pending')

    def _str_(self):
        return f"{self.pickup_id} - {self.customer}"


class Handlers(models.Model):
    id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=255)
    password=models.CharField(max_length=255)
    phone_number=models.CharField(max_length=15,unique=True,error_messages={
        'unique':"A person with this phone number already exists."
    })
    email=models.EmailField(unique=True, error_messages={
        'unique':"A person with this email already exists."
    })
    def __str__(self):
        return f"{self.name} - {self.id}"
    

class Staff(models.Model):
    STATUS_CHOICES=[
        ('Engaged','Engaged'),
        ('Free to pick','Free to pick')
    ]
    name=models.CharField(max_length=100)
    password=models.CharField(max_length=128)  # Use Django's built-in password hashing
    email=models.EmailField(unique=True)  # Unique email
    phone_number=models.CharField(max_length=15,unique=True)  # Unique phone number
    status=models.CharField(max_length=20,choices=STATUS_CHOICES,default='Free to pick')

    def __str__(self):
        return f"{self.name} - {self.id}"
    


class CompletedPickup(models.Model):
    Completed_Pickid=models.AutoField(primary_key=True)
    Staff_name=models.CharField(max_length=255)
    Staff_ID=models.IntegerField()

    def __str__(self):
        return f"{self.Completed_Pickid} - {self.Staff_name}"
    

class Assigned(models.Model):
    staff_id=models.IntegerField(primary_key=True)
    staff_name=models.CharField(max_length=255)
    pickup_id=models.IntegerField()
    assigned_at=models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"Pickup {self.pickup_id} assigned to {self.staff_name}"