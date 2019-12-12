from django.urls import path
from .views import (
    UsuarioList,
    UsuarioCreate,
    UsuarioUpdate,
    ProveedorList,
    ProveedorCreate,
    ProveedorUpdate,
    ProveedorDelete,
    ClienteList,
    ClienteCreate,
    ClienteUpdate,
)

urlpatterns = [
    path('usuarios/', UsuarioList.as_view(), name='usuario_lista'),
    path('usuarios/nuevo', UsuarioCreate.as_view(), name='usuario_nuevo'),
    path('usuarios/editar/<int:pk>', UsuarioUpdate.as_view(), name='usuario_editar'),
    path('proveedores/', ProveedorList.as_view(), name='proveedor_lista'),
    path('proveedores/nuevo', ProveedorCreate.as_view(), name='proveedor_nuevo'),
    path('proveedores/editar/<int:pk>', ProveedorUpdate.as_view(), name='proveedor_editar'),
    path('proveedores/eliminar/<int:pk>', ProveedorDelete.as_view(), name='proveedor_eliminar'),
    path('clientes/', ClienteList.as_view(), name='cliente_lista'),
    path('clientes/nuevo', ClienteCreate.as_view(), name='cliente_nuevo'),
    path('clientes/editar/<int:pk>', ClienteUpdate.as_view(), name='cliente_editar'),
]
