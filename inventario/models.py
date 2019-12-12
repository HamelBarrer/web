from django.db import models


# Create your models here.
class Categoria(models.Model):
    nombre_categoria = models.CharField(max_length=30)
    estado = models.BooleanField(default=True)

    def __str__(self):
        return self.nombre_categoria

    def save(self):
        self.nombre_categoria = self.nombre_categoria.upper()
        super(Categoria, self).save()


class UnidadMedida(models.Model):
    tipo_unidad = models.CharField(max_length=30)
    estado = models.BooleanField(default=True)

    def __str__(self):
        return self.tipo_unidad

    def save(self):
        self.tipo_unidad = self.tipo_unidad.upper()
        super(UnidadMedida, self).save()


class MateriaPrima(models.Model):
    nombre_materi_prima = models.CharField(max_length=40)
    cantidad = models.CharField(max_length=3)
    unidad_medida = models.ForeignKey(UnidadMedida, on_delete=models.CASCADE)
    fecha_creacion = models.DateField(auto_now=False, auto_now_add=True)
    estado = models.BooleanField(default=True)

    def __str__(self):
        return self.nombre_materi_prima

    def save(self):
        self.nombre_materi_prima = self.nombre_materi_prima.upper()
        super(MateriaPrima, self).save()


class Producto(models.Model):
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    nombre_producto = models.CharField(max_length=30)
    cantidad = models.CharField(max_length=3)
    estado = models.BooleanField(default=True)

    def __str__(self):
        return self.nombre_producto

    def save(self):
        self.nombre_producto = self.nombre_producto.upper()
        super(Producto, self).save()
