from django.db import models
from django.contrib.auth.models import User
import uuid

# Create your models here.
class Profile(models.Model):
    id = models.UUIDField(primary_key=True, db_index=True, default=uuid.uuid4, editable=False)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to="profiles/", verbose_name="Profil Resmi", default='profiles/default-profile.jpeg')
    bio = models.TextField(verbose_name="Hakkımda", default="Merhaba ben bir blog yazarıyım")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Katılma Tarihi")
    follow = models.ManyToManyField('self', verbose_name="Takip Edilenler", related_name="takip", blank=True, symmetrical=False) # symetrical 
    follower = models.ManyToManyField('self', verbose_name="Takipçiler", related_name="takipciler", blank=True, symmetrical=False)
    def __str__(self):
        return self.user.username
    
    class Meta:
        verbose_name_plural = "Profiller"
        verbose_name = "Profil"
        ordering = ['-created_at']
        
# class Istek(models.Model):
#     gonderen = models.ForeignKey(User, on_delete=models.CASCADE)
#     istekAlan = models.ForeignKey(User, on_delete=models.CASCADE, related_name="istek alan")
#     onay = models.BooleanField(default=False)
        
    
    
        
