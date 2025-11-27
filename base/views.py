from django.shortcuts import render, redirect
from .models import Room
# Create your views here.
from .forms import RoomForm

def home(request):
    
    return render(request, "base/home.html")
def room(request):
    rooms = Room.objects.all()
    context = {'rooms': rooms}
    return render(request, "base/room.html", context)

def createRoom(request):
    form = RoomForm()
    if request.method== 'POST':
        form = RoomForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    context = {"form":form}
    return render(request, "base/room_form.html", context)

def updateRoom(request, pk):
    room = Room.objects.get(id=pk)
    form = RoomForm(instance=room)
    if request.method=='POST':
        form = RoomForm(request.POST, instance=room)
        
        if form.is_valid():
            form.save()
            return redirect('room')

    context = {'form':form}
    return render(request, 'base/room_form.html', context)

def deleteRoom(request,pk):
    room = Room.objects.get(id=pk)

    if request.method == 'POST':
        room.delete()
        return redirect('room')
    context = {'obj':room}
    return render(request, 'base/deleteRoom.html', context)