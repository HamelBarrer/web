from django.urls import reverse_lazy
from django.views import generic
from .forms import (
    ProduccionForm
)
from .models import (
    Produccion
)
# Create your views here.
class ProduccionList(generic.ListView):
    model = Produccion
    context_object_name = 'obj'
    template_name = 'produccion_lista.html'

class ProduccionCreate(generic.CreateView):
    model = Produccion
    context_object_name = 'obj'
    template_name = 'produccion_nuevo.html'
    form_class = ProduccionForm
    success_url = reverse_lazy('produccion:produccion_lista')

class ProduccionUpdate(generic.UpdateView):
    model = Produccion
    context_object_name = 'obj'
    form_class  = ProduccionForm
    template_name = 'produccion_nuevo.html'
    success_url = reverse_lazy('produccion:produccion_lista')

class TareaList(generic.ListView):
    model = Produccion
    context_object_name = 'obj'
    template_name = 'tareas.html'