from django.shortcuts import render, redirect
from .forms import UserForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .models import *
from posts.models import *
from posts.views import like
def register(request):
    form = UserForm()
    username = ""
    email = ""
    bio_form = ""
    if request.method == 'POST':
        #### ilk yöntem #####
        # form = UserForm(request.POST)
        # # print(request.POST)
        # # username = request.POST['username']
        # if form.is_valid():
        #     user = form.save(commit=False) # user objesini oluşturup değişkene atanıyor
        #     user.save() # obje kaydediliyor
        #     newProfile = Profile.objects.create(user = user) # oluşturulan user objesine profile'ı bağlıyoruz
        #     newProfile.save()
            # messages.success(request, 'Kullanıcı oluşturuldu. Giriş yapabilirsiniz')
            # return redirect('login')
            
        #### ikinci yöntem ####
        username = request.POST.get('username')
        email = request.POST.get('email')
        image_form = request.FILES.get('image')
        bio_form = request.POST.get('bio')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')
    
        if password1 == password2:
            if User.objects.filter(username = username).exists():
                messages.error(request, 'Kullanıcı adı zaten mevcut')
            elif len(password1) < 6:
                messages.error(request, 'Şifreniz en az 6 karakter olmalıdır')
            elif username.lower() in password1.lower():
                messages.error(request, 'Kullanıcı adınız ile şifreniz benzer olmamalıdır')
            # elif password1[0].upper() != password1[0]:
            elif password1.title() != password1:
                messages.error(request, 'Şifreniz büyük harf ile başlamalıdır')
            else:
                user = User.objects.create_user(username = username, email = email, password = password1)
                profile = Profile.objects.create(
                    user = user,
                    image = image_form,
                    bio = bio_form
                )
                user.save()
                profile.save()
                # login(request, user) # kullanıcıya direkt giriş yaptırır
                messages.success(request,'Başarılı bir şekilde kaydedildi.')
                return redirect('login')
        else:
            messages.error(request, 'Şifreler uyuşmuyor')

        
    context = {
        'form':form,
        'username':username,
        'email':email,
        'bio_form':bio_form
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
    
    if request.method == 'POST':
        if 'follow' in request.POST:
            if request.user.is_authenticated:
                myProfil = request.user.profile # kendi profilimiz
                if profil in myProfil.follow.all(): # bu kullanıcıyı takip ediyor muyuz
                    myProfil.follow.remove(profil) # kendi takibimizden çıkarmak için
                    profil.follower.remove(myProfil) # karşı tarafın takipçilerinden kendimizi çıkardık
                    messages.success(request, f"{profil} Hesabını Takipten Çıktınız")
                else:
                    myProfil.follow.add(profil) # takibe aldık
                    profil.follower.add(myProfil) # karşı tarafın takipçilerine kendimizi ekledik
                    messages.success(request, f'{profil} Hesabını Takip etmeye başladınız')
                profil.save()
                myProfil.save()
            else:
                messages.warning(request, 'Giriş yapmalısınız')
                return redirect(f"/user/login/?next={request.path}")
        else:
            like(request)
        return redirect('profile', profilId = profil.id)
    context = {
        'profil':profil,
        'blogs':blogs
    }
    return render(request, 'user/profile.html', context)