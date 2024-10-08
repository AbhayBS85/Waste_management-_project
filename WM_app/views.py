from django.contrib.messages import constants as message_constants
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404
from django.shortcuts import render,redirect
from django.db.models.functions import Cast
from django.http import HttpResponse
from django.http import JsonResponse
from django.contrib.auth import logout
from django.http import HttpResponseRedirect
from django.db.models import DateField
from django.contrib import messages
from django.utils import timezone
from django.urls import reverse
from datetime import timedelta
import razorpay
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
                messages.error(request,"Username already exists. Try another one.")
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

                messages.success(request, "Account created successfully!\n     Now please Re-Login")
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
                request.session['username']=user.username
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
            total_amount=int(manual_weight)*30
            payment_status=request.POST.get('payment_method')
        else:
            waste_weight=weight_option
            total_amount=0
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
            messages.success(request,'Pickup scheduled.Payment on pickup.')
            return redirect('successpage')
        elif weight_option=='Enter the weight manually' and manual_weight:
            if payment_status=='Pay Online':
                # return redirect('payment_page',{'amount':total_amount})
                return HttpResponseRedirect(f"{reverse('payment_page')}?amount={total_amount}")
            else:
                messages.success(request,'Pickup scheduled. Payment on pickup.')
                return redirect('successpage')
    return render(request,'dergradable_form.html')



def requiredindex(request):
    username= request.session.get('username',request.user.username) 
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
            total_amount=int(manual_weight)*30
            payment_status=request.POST.get('payment_method')
        else:
            waste_weight=weight_option
            total_amount=0
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
            messages.success(request,'Pickup scheduled. Payment on pickup.')
            return redirect('successpage')
        elif weight_option=='Enter the weight manually' and manual_weight:
            if payment_status=='Pay Online':
                return HttpResponseRedirect(f"{reverse('payment_page')}?amount={total_amount}")
            else:
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
        print(f"Weight Option: {weight_option}, Manual Weight: {manual_weight}, Payment Status: {request.POST.get('payment_method')}")

        if weight_option=='Enter the weight manually' and manual_weight:
            waste_weight=manual_weight
            total_amount=int(manual_weight)*30
            payment_status=request.POST.get('payment_method')
            print(f"Payment Status Retrieved: {payment_status}")
        else:
            waste_weight=weight_option
            total_amount=0
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
        print("Weight Option: ", weight_option)
        print("Manual Weight: ", manual_weight)
        print("Payment Status: ", payment_status)
        print("Total Amount: ", total_amount)

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
        print(f"Payment Status Before Check: {payment_status}, Total Amount: {total_amount}")

        if weight_option=='Check on pickup':
            messages.success(request,'Pickup scheduled. Payment on pickup.')
            return redirect('successpage')
        elif weight_option=='Enter the weight manually' and manual_weight:
            print("Proceeding with manual weight and payment")
            if payment_status=='Pay online':
                print(f"Redirecting to payment page with amount: {total_amount}")
                return HttpResponseRedirect(f"{reverse('payment_page')}?amount={total_amount}")
            else:
                messages.success(request,'Pickup scheduled. Payment on pickup.')
                return redirect('successpage')
    return render(request,"hazardous.html")

def success(request):
    return render(request,"success.html")

def payment(request):
    if 'amount' in request.GET:
        amount=int(request.GET.get('amount'))*100 
        order_currency='INR'
        client=razorpay.Client(
            auth=("rzp_test_SROSnyInFv81S4", "WIWYANkTTLg7iGbFgEbwj4BM"))
    return render(request,"paymentpage.html",{'r':amount})


def successpayment(request):
    return render(request,"payment_confirm.html")

def admindashboard(request):
    return render(request,"admin_dashboard.html")


def pickupassign(request,pickup_id):
    free_staff=Staff.objects.filter(status='Free to pick')
    return render(request,"assign.html",{'staff':free_staff,'pickup_id':pickup_id})



def wastepickup(request):
    now=timezone.now() 
    start_of_day=now.replace(hour=0,minute=0,second=0,microsecond=0)
    todays_pickups=Pickup.objects.filter(date__gte=start_of_day,date__lte=now, pickup_status='Pending')
    return render(request,"pickup.html",{'pickups':todays_pickups})



def staffprofile(request):
    staff_id=request.session.get('staff_id')
    pickup_id=request.session.get('pickup_id')
    if staff_id:
        staff=Staff.objects.get(id=staff_id)
        pickup=Pickup.objects.get(pickup_id=pickup_id) if pickup_id else None
        return render(request,"staff.html",{'staff':staff,'pickup': pickup})
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
        messages.success(request,"Staff data successfully deleted.")
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
    if request.method=="POST":
        new_status=request.POST.get('status')
        staff_id= request.session.get('staff_id')
        if staff_id:
            staff=get_object_or_404(Staff,id=staff_id)
            if new_status in ['Engaged','Free to pick']:
                staff.status=new_status
                staff.save()
                return JsonResponse({"message":"Status updated successfully!"})
            else:
                return JsonResponse({"message":"Invalid status"},status=400)
        else:
            return JsonResponse({"message":"Staff not logged in"},status=403)
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


def staff_logout(request):
    staff_id=request.session.get('staff_id')
    if staff_id:
        staff=get_object_or_404(Staff,id=staff_id)
        staff.status='Offline'
        staff.save()
    logout(request)
    return redirect('stafflog') 

def assign_pickup_to_staff(request, pickup_id,staff_id):
    staff=Staff.objects.get(id=staff_id)
    pickup=Pickup.objects.get(pickup_id=pickup_id)

    # Assign the pickup to the staff
    staff.status='Engaged'
    staff.save()

    # Store pickup details in session for the staff dashboard
    request.session['pickup_id']=pickup_id
    messages.success(request,"Pickup assigned successfully!")

    return redirect('adm_dash')  # Redirect to staff dashboard


def confirm_assign(request,pickup_id):
    pickup=Pickup.objects.get(pickup_id=pickup_id)
    if request.method=='POST':
        staff_id=request.POST.get('staff_id')
        staff_name=request.POST.get('staff_name')
    # Logic for confirming the pickup assignment
        if staff_id and staff_name:
            assigned,created=Assigned.objects.update_or_create(
                staff_id=staff_id,
                defaults={
                    'staff_name': staff_name,
                    'pickup_id': pickup_id,
                    'assigned_at':timezone.now(),
                }
            )
            pickup.pickup_status = 'Assigned'
            pickup.save()
            if created:
                messages.success(request, 'Pickup assigned successfully.')
            else:
                messages.success(request, 'Pickup assignment updated successfully.')
            return redirect('staff')
        else:
            messages.error(request, 'Please fill in all fields.')
    # Any additional confirmation logic...
    return render(request,"staff_confirm_assign.html",{'pickup': pickup})


def finish_pickup(request, pickup_id):
    pickup=get_object_or_404(Pickup,pickup_id=pickup_id)

    if request.method=='POST':
        staff_name=request.POST.get('staff_name')
        staff_id=request.POST.get('staff_id')
        staff=get_object_or_404(Staff,id=staff_id)

        if staff_name and staff_id:
            completed_pickup=CompletedPickup.objects.create(
                Pickup_ID=pickup.pickup_id,
                Staff_name=staff_name,
                Staff_ID=staff_id
            )
            completed_pickup.save()
            staff.status='Free to pick'
            staff.save()

            pickup.pickup_status='Completed'
            pickup.save()
            messages.success(request,'Pickup completed successfully.')
            return redirect('staff')
        else:
            messages.error(request,'Please fill in all fields.')
    return render(request,'finish_pickup.html',{'pickup': pickup})


def assigned_pickups(request):
    today=timezone.now().date()
    assigned_pickups_today=Assigned.objects.filter(assigned_at__date=today).order_by('-assigned_at')
    context={
        'assigned_pickups':assigned_pickups_today
    }
    return render(request,'assigned.html',context)


def personal_pickup(request):
    completed_pickups=CompletedPickup.objects.all().order_by('-Completed_Pickid') 
    return render(request,"personal_pickup.html",{'completed_pickups':completed_pickups})


def completed_pickups(request):
    completed_pickup_ids=CompletedPickup.objects.values_list('Completed_Pickid',flat=True)
    Pickup.objects.filter(pickup_id__in=completed_pickup_ids).update(pickup_status='Completed')
    completed_pickups=Pickup.objects.filter(pickup_status='Completed').order_by('-date')
    context = {
        'completed_pickups': completed_pickups,
    }
    return render(request,"completed.html", context)


def edituser(request):
    if 'username' in request.session:
        username=request.session['username']
        try:
            user_data=UserData.objects.get(username=username)
        except UserData.DoesNotExist:
            return redirect('log')
        
        if request.method=='POST':
            new_email=request.POST.get('email')
            new_phone_number=request.POST.get('phone_number')
            new_address=request.POST.get('address')
            
            user_data.email=new_email
            user_data.phone_number=new_phone_number
            user_data.address=new_address
            user_data.save()

            messages.success(request, 'Your profile has been updated successfully!')
            
            return redirect('edit_user')
        context = {
            'username':user_data.username,
            'email':user_data.email,
            'phone_number':user_data.phone_number,
            'address':user_data.address,
        }
        return render(request,'edit_user.html',context)
    
    