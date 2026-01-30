from django.shortcuts import render, redirect
from .models import User

# Create your views here.

def login_(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        
        print(f"Login attempt - email: {email}, password: {password}")
        
        try:
            user = User.objects.get(email=email)
            print(f"User found: {user.email}")
            
            if hasattr(user, 'check_password') and user.check_password(password):
                print(f"Password matched (hashed)")
                request.session['user_id'] = user.id
                request.session['user_email'] = user.email
                return redirect('room')
            elif user.password == password:
                print(f"Password matched (plain-text)")
                request.session['user_id'] = user.id
                request.session['user_email'] = user.email
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
        
        if username and email and password:
            User.objects.create(username=username, email=email, password=password)
            return redirect('login')
        else:
            return redirect(request.path)

    return render(request, "register.html")

def logout_(request):
    request.session.flush()
    return redirect('/')