from .models import Blog
from django.forms import ModelForm


class BlogForm(ModelForm):
    class Meta:
        model = Blog
        fields = ['title', 'content', 'kategori', 'image']
        
    def __init__(self, *args, **kwargs):
        super(BlogForm, self).__init__(*args, **kwargs)
        for name, field in self.fields.items():
            field.widget.attrs.update({'class':'form-control'})