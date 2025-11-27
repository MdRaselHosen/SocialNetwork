from django.urls import path,include
from . import views
urlpatterns = [
    path("", views.home, name="home"),
    path("room", views.room, name='room'),
    # path("room_page/<str:pk>", views.room_page, name="room-page"),
    path("createRoom", views.createRoom, name='create-room'),
    path("updateRoom/<str:pk>", views.updateRoom, name='update-room'),
    path("deleteRoom/<str:pk>", views.deleteRoom, name='delete-room'),
]