from django.contrib import admin
from .models import Blog, Kategori, AltKategori


class BlogAdmin(admin.ModelAdmin):
    list_display = ['owner', 'title', 'created_at']
    list_display_links = ['owner', 'title']
    list_filter = ['owner', 'created_at']
    search_fields = ['owner__username']
    date_hierarchy = 'created_at'
    # list_editable = ['content']
    readonly_fields = ['created_at']
    list_per_page = 3
    

admin.site.register(Blog, BlogAdmin)
admin.site.register(Kategori)
admin.site.register(AltKategori)