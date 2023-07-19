from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name="index"),
    path('blog-detail/<str:pk>', detail, name='detail'),
    path('olustur/', create, name='create'),
]