from django.urls import reverse_lazy
from django.views import generic
from .forms import (
    PedidoMateriaPrimaForm,
    PedidoProductoForm,
)
from .models import (
    PedidoMateriaPrima,
    PedidoProducto,
)

from inicio.views import SinPrivilegios


# Create your views here.
class PedidoMateriaPrimaList(generic.ListView):
    model = PedidoMateriaPrima
    context_object_name = 'obj'
    template_name = 'pedido_materia_prima_lista.html'


class PedidoMateriaPrimaCreate(generic.CreateView):
    model = PedidoMateriaPrima
    context_object_name = 'obj'
    template_name = 'pedido_materia_prima_nuevo.html'
    form_class = PedidoMateriaPrimaForm
    success_url = reverse_lazy('pedido:pedido_materia_prima_lista')


class PedidoMateriaPrimaUpdate(generic.UpdateView):
    model = PedidoMateriaPrima
    form_class = PedidoMateriaPrimaForm
    context_object_name = 'obj'
    template_name = 'pedido_materia_prima_nuevo.html'
    success_url = reverse_lazy('pedido:pedido_materia_prima_lista')


class PedidoProductoList(generic.ListView):
    model = PedidoProducto
    context_object_name = 'obj'
    template_name = 'pedido_producto_lista.html'


class PedidoProductoCreate(generic.CreateView):
    model = PedidoProducto
    context_object_name = 'obj'
    template_name = 'pedido_producto_nuevo.html'
    form_class = PedidoProductoForm
    success_url = reverse_lazy('pedido:pedido_producto_lista')


class PedidoProductoUpdate(generic.UpdateView):
    model = PedidoProducto
    form_class = PedidoProductoForm
    context_object_name = 'obj'
    template_name = 'pedido_producto_nuevo.html'
    success_url = reverse_lazy('pedido:pedido_producto_lista')
