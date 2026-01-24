from django.shortcuts import render

# Create your views here.
def login_(request):
    return render(request, "login.html")

def register(request):
    return render(request, "register.html")

def logout_(request):
    return render(request, "logout.html")