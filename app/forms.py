from dataclasses import fields
from django import forms
from .models import Contacto, Producto
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class ContactoForm(forms.ModelForm):

    # nombre = forms.CharField(widget=forms.TextInput(attrs={"class":"form-control"}))
    

    class Meta:
        model = Contacto
        # fields = ["nombre", "corre", "tipo_consulta", "mensaje", "avisos"]
        fields = '__all__'
        
class ProductoForm(forms.ModelForm):

    class Meta:
        model = Producto
        fields = '__all__'

        widget = {
            "fecha_fabriacion": forms.SelectDateWidget()
        }

class CustomUserCreationForm(UserCreationForm):
    


    class Meta:
        model = User
        fields = ['username', "first_name", "last_name", "email", "password1", "password2"]
