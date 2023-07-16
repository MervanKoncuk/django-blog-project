from .models import Kategori

def get_category(request):
    kategoriler = Kategori.objects.all()
    context = {
        'kategoriler':kategoriler
    }
    return context

