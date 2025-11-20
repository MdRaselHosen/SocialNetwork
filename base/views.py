from django.shortcuts import render

# Create your views here.

rooms = [
    {'id':1, 'name':'Md. Rasel Hosen'},
    {'id':2, 'name': 'Md. Nasir Uddin'},
    {'id':3, 'name': 'Redwanul karim sany'}

]
def home(request):
    
    return render(request, "base/home.html")
def room(request):
    context = {'rooms': rooms}
    return render(request, "base/room.html", context)

def room_page(request,pk):
    room = None
    for i in rooms:
        if i['id']==int(pk):
            room = i
    context = {'room': room}
    return render(request, 'base/room_page.html', context)