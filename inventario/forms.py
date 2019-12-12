from django import forms
from .models import (
    Categoria,
    UnidadMedida,
    MateriaPrima,
    Producto,
)


class CategoriaForm(forms.ModelForm):
    class Meta:
        model = Categoria
        fields = ['nombre_categoria', 'estado']
        labels = {
            'nombre_categoria': 'Categoria',
            'estado': 'Estado'
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class': 'form-control'
            })


class UnidadMedidaForm(forms.ModelForm):
    class Meta:
        model = UnidadMedida
        fields = ['tipo_unidad', 'estado']
        labels = {
            'tipo_unidad': 'Tipo de Unidad',
            'estado': 'Estado'
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class': 'form-control'
            })


class MateriaPrimaForm(forms.ModelForm):
    unidad_medida = forms.ModelChoiceField(queryset=UnidadMedida.objects.filter(estado=True).order_by('tipo_unidad'))

    class Meta:
        model = MateriaPrima
        fields = ['nombre_materi_prima', 'cantidad', 'unidad_medida', 'estado']
        labels = {
            'nombre_materi_prima': 'Nombre Materia Prima',
            'cantidad': 'Cantidad',
            'estado': 'Estado',
        }
        widgets = {
            'cantidad': forms.NumberInput()
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class': 'form-control'
            })


class ProductoForm(forms.ModelForm):
    categoria = forms.ModelChoiceField(queryset=Categoria.objects.filter(estado=True).order_by('nombre_categoria'))

    class Meta:
        model = Producto
        fields = ['categoria', 'nombre_producto', 'cantidad', 'estado']
        labels = {
            'categoria': 'Categoria',
            'nombre_producto': 'Nombre Producto',
            'cantidad': 'Cantidad',
            'estado': 'Estado'
        }
        widgets = {
            'cantidad': forms.NumberInput()
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class': 'form-control'
            })
