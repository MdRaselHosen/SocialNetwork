
from django.urls import path,include
from . import views
urlpatterns = [
    path("login", views.login_, name="login_")
]