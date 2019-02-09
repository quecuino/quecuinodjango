from django import forms
from quecuino.models import Usuari, Recepta
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
        fields = [ 'nom','cognom','sexe','datanaixament','email', ]
        labels ={'nom':'Nom',
                 'cognom':'Cognom',
                 'sexe':'Sexe',
                 'datanaixament':'Data naixament'
                 }
        widgets = {
            'datanaixament':forms.DateInput()
        }


class Formreceta(forms.ModelForm):

    class Meta:
        model = Recepta
        fields =[ 'nom_recepta', 'descripcio', 'ingredients', 'procediment','imatge']



    #def __init__(self, *args, **kwargs):
     #   self._user = kwargs.pop('nom_user')
      #  super(Formreceta, self).__init__(*args, **kwargs)
    #def save(self, commit=True):
     #   inst = super(Formreceta, self).save(commit=False)
       # inst.nom_user = self._user
       # if commit:
        #    inst.save()
         #   self.save_m2m()
       # return inst




