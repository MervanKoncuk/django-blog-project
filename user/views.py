from django.shortcuts import render, redirect
from .forms import UserForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .models import *
from posts.models import *
def register(request):
    form = UserForm()
    if request.method == 'POST':
        form = UserForm(request.POST)
        # print(request.POST)
        # username = request.POST['username']
        if form.is_valid():
            form.save()
            messages.success(request, 'Kullanıcı oluşturuldu. Giriş yapabilirsiniz')
            return redirect('login')
        
    context = {
        'form':form
    }
    return render(request, 'user/register.html', context)

def userLogin(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        user = authenticate(request, username = username, password = password)
        next = request.GET.get('next')
        if user is not None:
            login(request, user)
            messages.success(request, 'Giriş yapıldı')
            if next:
                return redirect(next)
            else:
                return redirect('index')
        else:
            messages.error(request, 'Kullanıcı adı veya şifre hatalı')
        
    return render(request, 'user/login.html')

def userLogout(request):
    logout(request)
    messages.success(request, 'Çıkış yapıldı')
    return redirect('index')


# profile
def profile(request, profilId):
    profil = Profile.objects.get(id = profilId)
    blogs = Blog.objects.filter(owner = profil.user)
    context = {
        'profil':profil,
        'blogs':blogs
    }
    return render(request, 'user/profile.html', context)