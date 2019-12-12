import json
from django.shortcuts import render
from django.views.generic import TemplateView
from pedido.models import (
    Producto,
    PedidoProducto,
)
# Create your views here.


def grafico(request):
    template_name = 'grafico.html'
    queryset = PedidoProducto.objects.all()
    queryset1 = Producto.objects.all()
    producto = [obj.nombre_producto for obj in queryset1]
    cantidad = [int(obj.cantidad) for obj in queryset]
    
    context = {
        'producto': json.dumps(producto),
        'cantidad': json.dumps(cantidad),
    }

    return render(request, template_name, context)
