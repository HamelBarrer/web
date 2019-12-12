from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import (
    ListView,
    CreateView,
    UpdateView,
    DeleteView,
)
from .models import (
    Usuario,
    Proveedor,
    Cliente,
    Satelite,
    Administrador,
)
from .forms import (
    UsuarioForm,
    ProveedorForm,
    ClienteForm,
)

from inicio.views import SinPrivilegios


# Create your views here.
class UsuarioList(ListView):
    model = Usuario
    context_object_name = 'obj'
    template_name = 'usuario_lista.html'


class UsuarioCreate(CreateView):
    model = Usuario
    form_class = UsuarioForm
    context_object_name = 'obj'
    template_name = 'usuario_nuevo.html'
    success_url = reverse_lazy('usuario:usuario_lista')


class UsuarioUpdate(UpdateView):
    model = Usuario
    form_class = UsuarioForm
    context_object_name = 'obj'
    template_name = 'usuario_nuevo.html'
    success_url = reverse_lazy('usuario:usuario_lista')


class ProveedorList(ListView):
    model = Proveedor
    template_name = 'proveedor_lista.html'
    context_object_name = 'obj'


class ProveedorCreate(CreateView):
    model = Proveedor
    form_class = ProveedorForm
    context_object_name = 'obj'
    template_name = 'proveedor_nuevo.html'
    success_url = reverse_lazy('usuario:proveedor_lista')


class ProveedorUpdate(UpdateView):
    model = Proveedor
    form_class = ProveedorForm
    context_object_name = 'obj'
    template_name = 'proveedor_nuevo.html'
    success_url = reverse_lazy('usuario:proveedor_lista')


class ProveedorDelete(DeleteView):
    model = Proveedor
    form_class = ProveedorForm
    context_object_name = 'obj'
    template_name = 'eliminar.html'
    success_url = reverse_lazy('usuario:proveedor_lista')


class ClienteList(ListView):
    model = Cliente
    template_name = 'cliente_lista.html'
    context_object_name = 'obj'


class ClienteCreate(CreateView):
    model = Cliente
    form_class = ClienteForm
    context_object_name = 'obj'
    template_name = 'cliente_nuevo.html'
    success_url = reverse_lazy('usuario:cliente_lista')


class ClienteUpdate(UpdateView):
    model = Cliente
    form_class = ClienteForm
    template_name = 'cliente_nuevo.html'
    context_object_name = 'obj'
    success_url = reverse_lazy('usuario:cliente_lista')
