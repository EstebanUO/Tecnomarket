from dataclasses import fields
from django import forms
from .models import Contacto, Producto
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .validators import MaxSizeFileValidator
from django.forms import ValidationError

class ContactoForm(forms.ModelForm):

    # nombre = forms.CharField(widget=forms.TextInput(attrs={"class":"form-control"}))
    class Meta:
        model = Contacto
        # fields = ["nombre", "corre", "tipo_consulta", "mensaje", "avisos"]
        fields = '__all__'
        
class ProductoForm(forms.ModelForm):

    nombre = forms.CharField(min_length=3, max_length=50)
    imagen = forms.ImageField(required=False, validators=[MaxSizeFileValidator(max_file_size=2)])
    precio = forms.IntegerField(min_value=1, max_value=15000)

    def clean_nombre(self):
        nombre = self.cleaned_data["nombre"]
        existe = Producto.objects.filter(nombre__iexact=nombre).exists()

        if existe:
            raise ValidationError("Este nombre ya existe")

        return nombre
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
