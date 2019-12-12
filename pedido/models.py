from django.db import models
from django.db.models.signals import (
    post_save,
)
from django.dispatch import receiver
from django.db.models import Sum
from usuario.models import (
    Proveedor,
    Cliente,
)

from inventario.models import (
    Producto,
)


# Create your models here.
class PedidoMateriaPrima(models.Model):
    fecha_pedido = models.DateField(auto_now=False, auto_now_add=True)
    nombre_materia_prima = models.CharField(max_length=30)
    cantidad = models.IntegerField()
    proveedor = models.ForeignKey(Proveedor, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre_materia_prima


class PedidoProducto(models.Model):
    fecha_pedido = models.DateField(auto_now=False, auto_now_add=True)
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    cantidad = models.IntegerField()
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)

    def __str__(self):
        return self.producto


@receiver(post_save, sender=PedidoProducto)
def quitar_inventario(sender, instance, **kwargs):
    id_producto = instance.producto.id
    producto = Producto.objects.filter(pk=id_producto).first()
    if producto:
        cantidad = int(producto.cantidad) - int(instance.cantidad)
        producto.cantidad = cantidad
        producto.save()
