from django.shortcuts import render, redirect
from .models import *
from django.db.models import Q
from .forms import *
from django.contrib import messages
from django.contrib.auth.decorators import login_required
# Create your views here.
def like(request):
    if request.user.is_authenticated:
            blogId = request.POST.get('blogId')
            blog = Blog.objects.get(id = blogId)
            user = request.user.profile
            if 'like' in request.POST:
                if user in blog.like.all():
                    blog.like.remove(user)
                else:
                    blog.like.add(user)
                    blog.dislike.remove(user)
                    
            if 'dislike' in request.POST:
                if user in blog.dislike.all():
                    blog.dislike.remove(user)
                else:
                    blog.dislike.add(user)
                    blog.like.remove(user)
            blog.save()
    else:
        messages.warning(request, 'Giriş yapmanız gerekiyor')
            
def index(request):
    blogs = Blog.objects.all()
    print("Views")
    if request.method == 'POST':
        like(request)
        return redirect('index')
    # print(blogs)
    search = ''
    if request.GET.get('search'):
        search = request.GET.get('search')
        blogs = Blog.objects.filter(
            Q(title__icontains = search) |
            Q(kategori__name__icontains = search)
        )
    
    context = {
        'blogs':blogs,
        'search':search,
    }
    # for i in context['blogs']:
    #     print(i)
    #     print(i.id)
    #     print(i.content)
    return render(request, 'index.html', context)

# list tuple dict set string : iterable

def detail(request, pk):
    blog = Blog.objects.get(slug = pk)
    
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    if IpModel.objects.filter(ip = ip).exists():
        ipModel = IpModel.objects.get(ip = ip)
        
    else:
        ipModel = IpModel.objects.create(
            ip = ip
        )
        ipModel.save()
    blog.view.add(ipModel)

        # blog.view.add(request.user.profile)
    blog.save()
    print(blog)
    print(request)
    context = {
        'blog':blog
    }
    return render(request, 'detail-blog.html', context)



@login_required(login_url='/user/login/')
def create(request):
    form = BlogForm()
    if request.method == 'POST':
        form = BlogForm(request.POST, request.FILES)
        if form.is_valid():
            blog = form.save(commit=False) # obje oluşturuldu ancak veritabanına kaydedilmedi
            blog.owner = request.user
            blog.save() # değişiklik yapıldıktan sonra kaydedilip veritabanına gönderildi
            messages.success(request, 'Yazınız Oluşturuldu')
            return redirect('index')
    context = {
        'form':form
    }
    return render(request, 'create.html', context)
