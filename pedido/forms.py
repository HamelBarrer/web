from django import forms
from usuario.models import (
    Proveedor,
    Cliente,
)
from .models import (
    PedidoMateriaPrima,
    PedidoProducto,
)


class PedidoMateriaPrimaForm(forms.ModelForm):
    proveedor = forms.ModelChoiceField(queryset=Proveedor.objects.filter(estado=True).order_by('primer_nombre'))
    class Meta:
        model = PedidoMateriaPrima
        fields = ['nombre_materia_prima', 'cantidad', 'proveedor']
        labels = {
            'nombre_materia_prima': 'Nombre de materia prima'
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class': 'form-control'
            })


class PedidoProductoForm(forms.ModelForm):
    cliente = forms.ModelChoiceField(queryset=Cliente.objects.filter(estado=True).order_by('primer_nombre'))
    class Meta:
        model = PedidoProducto
        fields = ['producto', 'cantidad', 'cliente']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class': 'form-control'
            })
