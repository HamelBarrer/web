from django.contrib import admin
from .models import (
    Categoria,
    UnidadMedida,
    MateriaPrima,
    Producto,
)

# Register your models here.
admin.site.register(Categoria)
admin.site.register(UnidadMedida)
admin.site.register(MateriaPrima)
admin.site.register(Producto)
