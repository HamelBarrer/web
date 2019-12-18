from django.db import models

# Create your models here.
class Contacto(models.Model):
    nombre = models.CharField(max_length=100)
    telefono = models.CharField(max_length=10)
    correo = models.EmailField()

    def __str__(self):
        return self.nombre