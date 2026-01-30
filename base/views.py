from django.shortcuts import render, redirect
from .models import Room, Topic
# Create your views here.
from .forms import RoomForm
from django.db.models import Q

# def home(request):
#     topics = Topic.objects.all()
#     context = {'topics':topics}
    
#     return render(request, "base/home.html", context)

def room(request):
    q = request.GET.get('q') if request.GET.get('q')!= None else ''
    rooms = Room.objects.filter(
        Q(topic__name__icontains=q) |
        Q(name__icontains=q) |
        Q(description__icontains=q)
    )
    rooms_count = rooms.count()

    topics = Topic.objects.all()
    context = {'rooms': rooms, 'topics':topics, 'rooms_count': rooms_count}
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