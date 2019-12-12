from django.db import models
from usuario.models import (
    Satelite,
)
from inventario.models import (
    Producto,
    MateriaPrima,
)
# Create your models here.
class Produccion(models.Model):
    fecha_asignada = models.DateField(auto_now=False, auto_now_add=True)
    satelite = models.ForeignKey(Satelite, on_delete=models.CASCADE)
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    materia_prima = models.ForeignKey(MateriaPrima, on_delete=models.CASCADE)
    cantidad = models.IntegerField()
    fecha_entrega = models.DateField()

    def __str__(self):
        return self.satelite
