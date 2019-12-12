from django.db import models

# Create your models here.
class Reporte(models.Model):
    tipo_reporte = models.CharField(max_length=50)
    estado = models.BooleanField(default=True)

    def __str__(self):
        return self.tipo_reporte