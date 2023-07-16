from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to="profiles/", verbose_name="Profil Resmi")
    bio = models.TextField(verbose_name="Hakkımda")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Katılma Tarihi")
    def __str__(self):
        return self.user.username
    
    class Meta:
        verbose_name_plural = "Profiller"
        verbose_name = "Profil"
        ordering = ['-created_at']