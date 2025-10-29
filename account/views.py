from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth.models import User, auth
from django.contrib import messages

# Create your views here.

def login(request):
    if request.method == 'POST':
        userName = request.POST.get('username')
        password = request.POST.get('password') 

        user = auth.authenticate(username=userName, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            messages.warning(request,"Invalid Credentials")
            return redirect('login')
    else:
        return render(request, 'auth/login.html')

def register(request):
    if request.method == 'POST':
        userName = request.POST.get('username')
        password = request.POST.get('password') 
        password_confirmation = request.POST.get('password_confirmation') 
        email = request.POST.get('email')
        if password != password_confirmation:
            messages.warning(request,"Password not matching")
            return redirect('register')
        elif User.objects.filter(username=userName).exists():
            messages.warning(request,"Username already taken")
            return redirect('register') 
        elif User.objects.filter(email=email).exists():
            messages.warning(request,"Email already taken")
            return redirect('register') 
        else:
            user = User.objects.create_user(username=userName, password=password, email=email)
            user.save()
            messages.success(request,"User created successfully")
            return redirect('login')    
    else:
        return render(request, 'auth/register.html')

def logout(request):
    auth.logout(request)
    return redirect('/')