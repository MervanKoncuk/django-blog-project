from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class UserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','first_name', 'email', 'password1', 'password2']
    
    def __init__(self, *args, **kwargs): # constructor
        super(UserForm, self).__init__(*args, **kwargs)
        for name, field in self.fields.items():
            field.widget.attrs.update({'class':'form-control'})
            # field.help_text = ""
            
        # self.fields['username'].help_text = "Kullanıcı adınızı giriniz. Özel karakter kullanmayın"
        
        
