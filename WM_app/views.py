from django.contrib.auth.decorators import login_required
from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth import logout
from django.contrib import messages
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

        biowaste=Biowaste(
            username=name,
            contact_no=phone,
            waste_type=waste_type,
            waste_weight=waste_weight,
            manual_weight=manual_weight if manual_weight else None,
            address=address
        )
        biowaste.save()

        return redirect('successpage')
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

        biowaste=NonBiowaste(
            username=name,
            contact_no=phone,
            waste_type=waste_type,
            waste_weight=waste_weight,
            manual_weight=manual_weight if manual_weight else None,
            address=address
        )
        biowaste.save()

        return redirect('successpage')
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

        biowaste=Hazardouswaste(
            username=name,
            contact_no=phone,
            waste_type=waste_type,
            waste_weight=waste_weight,
            manual_weight=manual_weight if manual_weight else None,
            address=address
        )
        biowaste.save()
        return redirect('successpage')
    return render(request,"hazardous.html")

def success(request):
    return render(request,"success.html")

