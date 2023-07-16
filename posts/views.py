from django.shortcuts import render, redirect
from .models import *
from django.db.models import Q
from .forms import *
from django.contrib import messages
from django.contrib.auth.decorators import login_required
# Create your views here.
def index(request):
    blogs = Blog.objects.all()
    
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

def detail(request, blogId):
    blog = Blog.objects.get(id = blogId)
    print(blog)
    print(request)
    context = {
        'blog':blog
    }
    return render(request, 'detail-blog.html', context)



@login_required(login_url='/login/')
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
