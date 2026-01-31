from django.shortcuts import render, redirect
from .models import User
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required

# Create your views here.

def login_(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        
        try:
            user = User.objects.get(email=email)
            
            if hasattr(user, 'check_password') and user.check_password(password):
                login(request, user)
                return redirect('room')
            elif user.password == password:
                login(request, user)
                return redirect('room')
            else:
                return render(request, "login.html", {'error': 'Invalid credentials'})
        except User.DoesNotExist:
            return render(request, "login.html", {'error': 'User not found'})

    return render(request, "login.html")

def register(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')

        user = User.objects.filter(email=email)
        if len(user)> 0:
            return redirect(request.path)
        
        if username and email and password:
            User.objects.create(username=username, email=email, password=password)
            return redirect('login')
        else:
            return redirect(request.path)

    return render(request, "register.html")

@login_required(login_url="user/login/")
def logout_(request):
    request.session.flush()
    return redirect('/')

@login_required(login_url="user/login/")
def profile(request):
    return render(request, 'profile.html')