from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify
from django.urls import reverse

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
    title = models.CharField(max_length=100) # type text Neos Yazılım Akademi
    content = models.TextField(verbose_name="İçerik", help_text="Buraya yazacağınız içerik bloğunuzun içeriği olacaktır") # textarea
    # price = models.IntegerField() # type number
    image = models.ImageField(upload_to = 'blogs/', null=True)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Oluşturulma Tarihi", null=True)
    like = models.ManyToManyField('user.Profile', related_name="beğeniler")
    dislike = models.ManyToManyField('user.Profile')
    view = models.ManyToManyField('posts.IpModel', related_name="goruntulenme", blank=True)
    slug = models.SlugField(null=True, blank=True, editable=False) # neos-yazilim-akademi
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.title.replace('ı', 'i'))
        # self.slug = self.title.lower().replace('ı', 'i').replace('ö', 'o').replace(' ', '-')
        super(Blog, self).save(*args, **kwargs)
        
    def get_absolute_url(self):
        return reverse('detail', kwargs={'pk':self.slug})
    

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


class IpModel(models.Model):
    ip = models.CharField(max_length=20)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.ip