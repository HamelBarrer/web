from django import forms
from usuario.models import (
    Satelite,
)
from .models import (
    Produccion,
)

class ProduccionForm(forms.ModelForm):
    class Meta:
        model = Produccion
        fields = ['satelite', 'producto', 'materia_prima', 'cantidad', 'fecha_entrega']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class': 'form-control'
            })