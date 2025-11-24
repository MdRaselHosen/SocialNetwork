from django.shortcuts import render
from .models import Room
# Create your views here.


def home(request):
    
    return render(request, "base/home.html")
def room(request):
    rooms = Room.objects.all()
    context = {'rooms': rooms}
    return render(request, "base/room.html", context)

def createRoom(request):
    context = {}
    return render(request, "base/room_form.html", context)
