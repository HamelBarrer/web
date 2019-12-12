from django.urls import path
from .views import (
    PedidoMateriaPrimaList,
    PedidoMateriaPrimaCreate,
    PedidoMateriaPrimaUpdate,
    PedidoProductoList,
    PedidoProductoCreate,
    PedidoProductoUpdate,
)

urlpatterns = [
    path('pedido_materia_prima/', PedidoMateriaPrimaList.as_view(), name='pedido_materia_prima_lista'),
    path('pedido_materia_prima/nueva', PedidoMateriaPrimaCreate.as_view(), name='pedido_materia_prima_nueva'),
    path('pedido_materia_prima/editar/<pk>', PedidoMateriaPrimaUpdate.as_view(), name='pedido_materia_prima_editar'),
    path('pedido_producto/', PedidoProductoList.as_view(), name='pedido_producto_lista'),
    path('pedido_producto/nueva', PedidoProductoCreate.as_view(), name='pedido_producto_nueva'),
    path('pedido_producto/editar/<pk>', PedidoProductoUpdate.as_view(), name='pedido_producto_editar'),
]
