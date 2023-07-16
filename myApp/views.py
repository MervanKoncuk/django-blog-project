from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
# Sayfalarımın görüntülenebilmesi için gerekli fonksiyonları yazacağımız dosya
def index(request):
    # print(request)
    return render(request, 'index.html')

def about(request):
    return render(request, 'hakkimizda.html')