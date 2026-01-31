from django.urls import path,include
from . import views
urlpatterns = [
    # path("", views.home, name="home"),
    path("", views.room, name='room'),
    # path("room_page/<str:pk>", views.room_page, name="room-page"),
    path("create-room", views.createRoom, name='create-room'),
    path("update-room/<str:pk>", views.updateRoom, name='update-room'),
    path("delete-room/<str:pk>", views.deleteRoom, name='delete-room'),
    path("post-details/<str:pk>", views.postDetails, name='post-details'),
]