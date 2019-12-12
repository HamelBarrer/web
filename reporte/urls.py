from django.urls import path
from .views import (
    ReporteList,
    ReporteCreate,
    ReporteUpdate,
)

urlpatterns = [
    path('tipo_reporte/', ReporteList.as_view(), name='tipo_reporte_lista'),
    path('tipo_reporte/nueva', ReporteCreate.as_view(), name='tipo_reporte_nueva'),
    path('tipo_reporte/editar/<pk>', ReporteUpdate.as_view(), name='tipo_reporte_editar'),
]