from django.db import models
from django.contrib.auth.models import User

# bu dosyada yapılan her değişiklikten sonra girilmesi gereken komutlar :
# python manage.py makemigrations
# python managae.py migrate 


class Kategori(models.Model):
    name = models.CharField(max_length=100)
    
    def __str__(self):
        return str(self.id)

class AltKategori(models.Model):
    name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name

# imageField kullanabilmek için : pip install Pillow

class Blog(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    kategori = models.ForeignKey(Kategori, on_delete=models.SET_NULL, null=True)
    alt = models.ManyToManyField(AltKategori)
    ornek = models.OneToOneField(Kategori, related_name="ornegim", on_delete=models.CASCADE, null=True, blank=True)
    title = models.CharField(max_length=100) # type text
    content = models.TextField(verbose_name="İçerik", help_text="Buraya yazacağınız içerik bloğunuzun içeriği olacaktır") # textarea
    # price = models.IntegerField() # type number
    image = models.ImageField(upload_to = 'blogs/', null=True)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Oluşturulma Tarihi", null=True)

# yazar
# oluşturulma tarihi
# like-dislike
# görüntülenme
# slug
# id (UUID)




    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name_plural = "Yazılar" # anabaşlık
        verbose_name = "Yazı" # tekil başlık
        # ordering = ['-id'] # sıralamayı değiştirmek için
        
        
# manytomany 
# manytoone = foreignkey
# onetoone