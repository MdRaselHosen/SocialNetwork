from django.shortcuts import render

# Create your views here.
def login_(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        print("user name is ", email, "password is ", password)
    return render(request, "login.html")

def register(request):
    return render(request, "register.html")

def logout_(request):
    return render(request, "logout.html")