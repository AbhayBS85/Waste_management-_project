from django.shortcuts import render

# Create your views here.
def indexpage(request):
    return render(request,'index.html')

def signuppage(request):
    return render(request,'signup.html')

def loginpage(request):
    return render(request,'login.html')