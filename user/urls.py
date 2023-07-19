from django.urls import path
from .views import *

urlpatterns = [
    path('register/', register, name="register"),
    path('login/', userLogin, name='login'),
    path('logout/', userLogout, name='logout'),
    path('profile/<profilId>', profile, name='profile')
]