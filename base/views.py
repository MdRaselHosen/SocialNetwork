from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Room, Topic
from django.db.models import Q



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

def postDetails(requset, pk):
    post = Room.objects.get(pk=pk)

    return render(requset, "base/post-details.html")

@login_required(login_url="user/login/")
def createRoom(request):

    if request.method== 'POST':
        topic = request.POST.get('topic')
        title = request.POST.get('title')
        desc = request.POST.get('description')

        topic_obj, created = Topic.objects.get_or_create(name=topic)
        Room.objects.create(
            host = request.user,
            topic = topic_obj,
            name = title,
            description = desc
        )
        return redirect('room')

    topics = Topic.objects.all()
    context = {"topics":topics}
    return render(request, "base/room_form.html", context)

@login_required(login_url="user/login/")
def updateRoom(request, pk):
    room = Room.objects.get(id=pk)
    topics = Topic.objects.all()

    if request.method == 'POST':
        room.topic.name = request.POST.get('topic')
        room.name = request.POST.get('title')
        room.description = request.POST.get('description')

        if getattr(request, 'user', None) and request.user.is_authenticated:
            room.host = request.user
        room.save()

        return redirect('room')

    
    context = {'room': room, 'topics': topics, 'page':'update'}
    return render(request, 'base/room_form.html', context)

@login_required(login_url="user/login/")
def deleteRoom(request,pk):
    room = Room.objects.get(id=pk)

    if request.method == 'POST':
        room.delete()
        return redirect('room')
    context = {'obj':room}
    return render(request, 'base/deleteRoom.html', context)