from django import forms
from quecuino.models import Usuari
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
class FormUser(UserCreationForm):
    class Meta:
        model=User

        fields = [
            'username','password1','password2'
        ]
        def save(self, commit=True):
            user = super(self).save(commit=False)
            if commit:
                user.save()
            return user

class FormUserextendido(forms.ModelForm):
    class Meta:
        model = Usuari
        fields = [ 'nom','cognom','sexe','datanaixament','email' ]
        labels ={'nom':'Nom',
                 'cognom':'Cognom',
                 'sexe':'Sexe',
                 'datanaixament':'Data naixament'
                 }
        widgets = {
            'datanaixament':forms.DateInput()
        }

