from django.urls import reverse_lazy
from django.views import generic
from .models import (
    Categoria,
    UnidadMedida,
    MateriaPrima,
    Producto,
)
from .forms import (
    CategoriaForm,
    UnidadMedidaForm,
    MateriaPrimaForm,
    ProductoForm,
)
from inicio.views import SinPrivilegios


# Create your views here.
class CategoriaList(generic.ListView):
    model = Categoria
    context_object_name = 'obj'
    template_name = 'categoria_lista.html'


class CategoriaCreate(generic.CreateView):
    model = Categoria
    context_object_name = 'obj'
    template_name = 'cliente_nuevo.html'
    form_class = CategoriaForm
    success_url = reverse_lazy('inventario:categoria_lista')


class CategoriaUpdate(generic.UpdateView):
    model = Categoria
    form_class = CategoriaForm
    context_object_name = 'obj'
    template_name = 'categoria_nuevo.html'
    success_url = reverse_lazy('inventario:categoria_lista')


class UnidadMedidaList(generic.ListView):
    model = UnidadMedida
    context_object_name = 'obj'
    template_name = 'unidad_medida_lista.html'


class UnidadMedidaCreate(generic.CreateView):
    model = UnidadMedida
    context_object_name = 'obj'
    template_name = 'unidad_medida_nuevo.html'
    form_class = UnidadMedidaForm
    success_url = reverse_lazy('inventario:unidad_medida_lista')


class UnidadMedidaUpdate(generic.UpdateView):
    model = UnidadMedida
    form_class = UnidadMedidaForm
    context_object_name = 'obj'
    template_name = 'unidad_medida_nuevo.html'
    success_url = reverse_lazy('inventario:unidad_medida_lista')


class MateriaPrimaList(generic.ListView):
    model = MateriaPrima
    context_object_name = 'obj'
    template_name = 'materia_prima_lista.html'


class MateriaPrimaCreate(generic.CreateView):
    model = MateriaPrima
    context_object_name = 'obj'
    template_name = 'materia_prima_nuevo.html'
    form_class = MateriaPrimaForm
    success_url = reverse_lazy('inventario:materia_prima_lista')


class MateriaPrimaUpdate(generic.UpdateView):
    model = MateriaPrima
    form_class = MateriaPrimaForm
    context_object_name = 'obj'
    template_name = 'materia_prima_nuevo.html'
    success_url = reverse_lazy('inventario:materia_prima_lista')


class ProductoList(generic.ListView):
    model = Producto
    context_object_name = 'obj'
    template_name = 'producto_lista.html'


class ProductiCreate(generic.CreateView):
    model = Producto
    context_object_name = 'obj'
    template_name = 'producto_nuevo.html'
    form_class = ProductoForm
    success_url = reverse_lazy('inventario:producto_lista')


class ProductoUpdate(generic.UpdateView):
    model = Producto
    form_class = ProductoForm
    context_object_name = 'obj'
    template_name = 'producto_nuevo.html'
    success_url = reverse_lazy('inventario:producto_lista')
