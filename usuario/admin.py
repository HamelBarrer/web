from django.contrib import admin
from .models import (
    Usuario,
    Administrador,
    Satelite,
    Proveedor,
    Cliente,
)

# Register your models here.
admin.site.register(Usuario)
admin.site.register(Administrador)
admin.site.register(Satelite)
admin.site.register(Proveedor)
admin.site.register(Cliente)
