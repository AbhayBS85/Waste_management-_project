from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404
from django.shortcuts import render,redirect
from django.db.models.functions import Cast
from django.http import HttpResponse
from django.http import JsonResponse
from django.contrib.auth import logout
from django.db.models import DateField
from django.contrib import messages
from django.utils import timezone
from datetime import timedelta
from.models import*


# Create your views here.
def indexpage(request):
    return render(request,'index.html')

def signuppage(request):
    if request.method=='POST':
        fullname=request.POST['fullname1']
        username=request.POST['username1']
        address=request.POST['address1']
        email=request.POST['email1']
        phone=request.POST['phone1']
        password=request.POST['password1']
        re_password=request.POST['repassword1']

        try:
            # Check if the username already exists
            if UserData.objects.filter(username=username).exists():
                messages.error(request, "Username already exists. Try another one.")
                return redirect('signup')

            # Check if the email already exists
            elif UserData.objects.filter(email=email).exists():
                messages.error(request, "Email already in use. Try another email.")
                return redirect('signup')

            # Check if the phone number already exists
            elif UserData.objects.filter(phone_number=phone).exists():
                messages.error(request, "Phone number already exists. Try with another number.")
                return redirect('signup')

            # Check if the passwords match
            elif password!=re_password:
                messages.error(request,"The passwords don't match. Check and try again.")
                return redirect('signup')

            # If all checks pass, create a new user
            else:
                new_user=UserData(
                    fullname=fullname,
                    username=username,
                    address=address,
                    email=email,
                    password=password,  # Hash the password before saving
                    phone_number=phone
                )
                new_user.save()

                messages.success(request, "Your account has been created successfully!")
                return redirect('relog')  # Redirect to the success page after successful signup

        except Exception as e:
            # If any error occurs during the signup process, display a generic error message
            messages.error(request, "Account creation failed. Try again.")
            return redirect('sign')
    return render(request,'signup.html')


def loginpage(request):
    if request.method=='POST':
        username_or_phone=request.POST['username']  # Get the username or phone number from the form
        password=request.POST['password']  # Get the password from the form
        try:
            user=UserData.objects.get(
                username=username_or_phone,password=password
            ) or UserData.objects.get(
                phone_number=username_or_phone,password=password
            )
            if user:  # If a user is found
                # Authentication successful, redirect to the desired page
                return redirect('logre')
            
        except UserData.DoesNotExist:
            # If no matching user is found
            messages.error(request, "Login failed. Try again.")
            return redirect('log') 
            
    return render(request,'login.html')

def biode(request):
    if request.method=='POST':
        name=request.POST.get('name')
        phone=request.POST.get('phone')
        waste_type=request.POST.get('category')
        weight_option=request.POST.get('weight_option')
        manual_weight=request.POST.get('manual_weight')
        address=request.POST.get('address')

        if weight_option=='Enter the weight manually' and manual_weight:
            waste_weight=manual_weight
        else:
            waste_weight=weight_option
            payment_status='Cash on Pickup'

        biowaste=Biowaste(
            username=name,
            contact_no=phone,
            waste_type=waste_type,
            waste_weight=waste_weight,
            manual_weight=manual_weight if manual_weight else None,
            address=address
        )
        biowaste.save()
        pickup=Pickup(
            customer=name,
            contact_number=phone,
            waste_type=waste_type,
            weight=waste_weight,
            location=address,
            payment_status=payment_status,
            date=timezone.now()
        )
        pickup.save()

        if weight_option=='Check on pickup':
            return redirect('successpage')
        elif weight_option=='Enter the weight manually' and manual_weight:
            return redirect('payment_page')
    return render(request,'dergradable_form.html')

def requiredindex(request):
    username=request.user.username
    return render(request,'login_index.html',{'username': username})

def relogin(request):
    return render(request,'relogin.html')

def logout_view(request):
    logout(request)
    return render(request,"index.html")

def nonbiowaste(request):
    if request.method=='POST':
        name=request.POST.get('name1')
        phone=request.POST.get('phone2')
        waste_type=request.POST.get('category3')
        weight_option=request.POST.get('weight_option4')
        manual_weight=request.POST.get('manual_weight5')
        address=request.POST.get('address6')

        if weight_option=='Enter the weight manually' and manual_weight:
            waste_weight=manual_weight
        else:
            waste_weight=weight_option
            payment_status='Cash on Pickup'

        non_biowaste=NonBiowaste(
            username=name,
            contact_no=phone,
            waste_type=waste_type,
            waste_weight=waste_weight,
            manual_weight=manual_weight if manual_weight else None,
            address=address
        )
        non_biowaste.save()
        pickup=Pickup(
            customer=name,
            contact_number=phone,
            waste_type=waste_type,
            weight=waste_weight,
            location=address,
            payment_status=payment_status,
            date=timezone.now()
        )
        pickup.save()

        if weight_option=='Check on pickup':
            return redirect('successpage')
        elif weight_option=='Enter the weight manually' and manual_weight:
            return redirect('payment_page')
    return render(request,"nonbio.html")

def hazwaste(request):
    if request.method=='POST':
        name=request.POST.get('u_name')
        phone=request.POST.get('u_phone')
        waste_type=request.POST.get('u_category')
        weight_option=request.POST.get('u_weight_option')
        manual_weight=request.POST.get('u_manual_weight')
        address=request.POST.get('u_address')

        if weight_option=='Enter the weight manually' and manual_weight:
            waste_weight=manual_weight
        else:
            waste_weight=weight_option
            payment_status='Cash on Pickup'

        hazardwaste=Hazardouswaste(
            username=name,
            contact_no=phone,
            waste_type=waste_type,
            waste_weight=waste_weight,
            manual_weight=manual_weight if manual_weight else None,
            address=address
        )
        hazardwaste.save()
        pickup=Pickup(
            customer=name,
            contact_number=phone,
            waste_type=waste_type,
            weight=waste_weight,
            location=address,
            payment_status=payment_status,
            date=timezone.now()
        )
        pickup.save()

        if weight_option=='Check on pickup':
            return redirect('successpage')
        elif weight_option=='Enter the weight manually' and manual_weight:
            return redirect('payment_page')
    return render(request,"hazardous.html")

def success(request):
    return render(request,"success.html")

def payment(request):
    return render(request,"paymentpage.html")

def admindashboard(request):
    return render(request,"admin_dashboard.html")

def pickupassign(request):
    return render(request,"assign.html")

def wastepickup(request):
    now=timezone.now() 
    start_of_day=now.replace(hour=0,minute=0,second=0,microsecond=0)
    todays_pickups=Pickup.objects.filter(date__gte=start_of_day,date__lte=now)
    return render(request,"pickup.html",{'pickups':todays_pickups})

def staffprofile(request):
    staff_id=request.session.get('staff_id')
    if staff_id:
        staff=Staff.objects.get(id=staff_id)
        return render(request,"staff.html",{'staff':staff})
    else:
        return redirect('stafflog')

def newstaff(request):
    if request.method=='POST':
        name=request.POST['name']
        password=request.POST['password']
        email=request.POST['email']
        phone_number=request.POST['phone_number']
        if Staff.objects.filter(email=email).exists():
            messages.error(request,'Email ID already in use.')
            return redirect('add_staff') 
        elif Staff.objects.filter(phone_number=phone_number).exists():
            messages.error(request,'Phone number already exists. Try another one.')
            return redirect('add_staff')
        staff=Staff(name=name,password=password,email=email,phone_number=phone_number)
        staff.save()
        messages.success(request,'Staff added successfully!')
        return redirect('adm_dash')
    return render(request,"add_staff.html")


def deletestaff(request):
    staff_list=Staff.objects.all()
    staff_id=request.GET.get('id')
    if staff_id:
        Staff.objects.filter(id=staff_id).delete()
        return redirect('staff_management')
    return render(request,"delete_staff.html",{'staff_list': staff_list})

def staffedit(request):
    return render(request,"staff_edit.html")



def oldpickups(request):
    now=timezone.now()
    start_of_day=now.replace(hour=0,minute=0,second=0,microsecond=0)
    pickups=Pickup.objects.filter(date__lt=start_of_day).annotate(
        date_only=Cast('date',DateField())
    ).order_by('-date_only','-date')
    pickup_by_date={}
    for pickup in pickups:
        pickup_date=pickup.date_only
        if pickup_date not in pickup_by_date:
            pickup_by_date[pickup_date]=[]
        pickup_by_date[pickup_date].append(pickup)
    return render(request,"previous.html",{'pickup_by_date':pickup_by_date})

def update_status(request):
    if request.method=="POST" and request.is_ajax():
        new_status=request.POST.get('status')
        staff=get_object_or_404(Staff,id=request.user.id)
        staff.status=new_status
        staff.save()
        return JsonResponse({"message":"Status updated successfully!"})
    return JsonResponse({"message": "Invalid request"},status=400)


def staffsignin(request):
    if request.method=="POST":
        username=request.POST.get("username")
        password=request.POST.get("password")
        try:
            staff=Staff.objects.get(name=username)
            if staff.password==password:
                request.session['staff_id']=staff.id
                return redirect('staff')
            else:
                # Incorrect password
                messages.error(request,"Incorrect password")
        except Staff.DoesNotExist:
            # Username not found
            messages.error(request, "Incorrect username")
    return render(request,"stafflogin.html")