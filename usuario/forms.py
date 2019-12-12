from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.db import transaction
from .models import (
    Usuario,
    Satelite,
    Proveedor,
    Cliente,
)


class UsuarioForm(UserCreationForm):
    email = forms.EmailField(required=True, help_text='Requerido, con 254 caracteres maximo')
    class Meta:
        model = Usuario
        fields = [
            'username',
            'first_name',
            'last_name',
            'email',
            'is_active',
            'is_administrador',
            'is_satelite',
        ]
        labels = {
            'username': 'Nombre de Usuario',
            'first_name': 'Nombre',
            'last_name': 'Apellido',
            'email': 'Correo'
        }

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if Usuario.objects.filter(email=email):
            raise forms.ValidationError('El correo ya esta registrado')
        return email

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class': 'form-control'
            })


class SateliteForm(forms.ModelForm):
    class Meta:
        model = Satelite
        fields = ['nivel_acadademico']
        labels = {
            'nivel_acadademico': 'Nivel Educativo'
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class': 'form-control'
            })


class ProveedorForm(forms.ModelForm):
    class Meta:
        model = Proveedor
        fields = ['primer_nombre', 'segundo_nombre', 'primer_apellido', 'segundo_apellido', 'correo', 'telefono',
                  'estado', 'razon_social']
        labels = {
            'primer_nombre': 'Primer Nombre',
            'segundo_nombre': 'Segundo Nombre',
            'primer_apellido': 'Primer Apellido',
            'segundo_apellido': 'Segundo Apellido',
            'correo': 'Correo',
            'telefono': 'Telefono',
            'estado': 'Estado',
            'razon_social': 'Razon Social'
        }
        widgets = {
            'telefono': forms.NumberInput(),
            'estado': forms.CheckboxInput()
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class': 'form-control'
            })


class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ['primer_nombre', 'segundo_nombre', 'primer_apellido', 'segundo_apellido', 'correo', 'telefono',
                  'estado', 'razon_social']
        labels = {
            'primer_nombre': 'Primer Nombre',
            'segundo_nombre': 'Segundo Nombre',
            'primer_apellido': 'Primer Apellido',
            'segundo_apellido': 'Segundo Apellido',
            'correo': 'Correo',
            'telefono': 'Telefono',
            'estado': 'Estado',
            'razon_social': 'Razon Social'
        }
        widgets = {
            'telefono': forms.NumberInput(),
            'estado': forms.CheckboxInput()
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class': 'form-control'
            })
