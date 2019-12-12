from django.urls import path
from .views import (
    CategoriaList,
    CategoriaCreate,
    CategoriaUpdate,
    UnidadMedidaList,
    UnidadMedidaCreate,
    UnidadMedidaUpdate,
    MateriaPrimaList,
    MateriaPrimaCreate,
    MateriaPrimaUpdate,
    ProductoList,
    ProductiCreate,
    ProductoUpdate,
)

urlpatterns = [
    path('categorias/', CategoriaList.as_view(), name='categoria_lista'),
    path('categorias/nueva', CategoriaCreate.as_view(), name='categoria_nueva'),
    path('categorias/editar/<pk>', CategoriaUpdate.as_view(), name='categoria_editar'),
    path('unidad_medidas/', UnidadMedidaList.as_view(), name='unidad_medida_lista'),
    path('unidad_medidas/nueva', UnidadMedidaCreate.as_view(), name='unidad_medida_nueva'),
    path('unidad_medidas/editar/<pk>', UnidadMedidaUpdate.as_view(), name='unidad_medida_editar'),
    path('materia_primas/', MateriaPrimaList.as_view(), name='materia_prima_lista'),
    path('materia_primas/nueva', MateriaPrimaCreate.as_view(), name='materia_prima_nueva'),
    path('materia_primas/editar/<pk>', MateriaPrimaUpdate.as_view(), name='materia_prima_editar'),
    path('productos/', ProductoList.as_view(), name='producto_lista'),
    path('productos/nueva', ProductiCreate.as_view(), name='producto_nueva'),
    path('productos/editar/<pk>', ProductoUpdate.as_view(), name='producto_editar'),
]
