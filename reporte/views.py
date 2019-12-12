from django.urls import reverse_lazy
from django.views import generic
from .forms import (
    ReporteForm
)
from .models import (
    Reporte
)
# Create your views here.
class ReporteList(generic.ListView):
    model = Reporte
    context_object_name = 'obj'
    template_name = 'reporte_lista.html'

class ReporteCreate(generic.CreateView):
    model = Reporte
    form_class = ReporteForm
    context_object_name = 'obj'
    template_name = 'reporte_nuevo.html'
    success_url = reverse_lazy('reporte:tipo_reporte_lista')

class ReporteUpdate(generic.UpdateView):
    model = Reporte
    form_class = ReporteForm
    context_object_name = 'obj'
    template_name = 'reporte_nuevo.html'
    success_url = reverse_lazy('reporte:tipo_reporte_lista')