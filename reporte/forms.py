from django import forms
from .models import (
    Reporte,
)


class ReporteForm(forms.ModelForm):
    class Meta:
        model = Reporte
        fields = ['tipo_reporte', 'estado']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class': 'form-control'
            })
