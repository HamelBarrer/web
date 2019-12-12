from django.urls import path
from .views import (
    ProduccionList,
    ProduccionCreate,
    ProduccionUpdate,
    TareaList
)
urlpatterns = [
    path('produccion/', ProduccionList.as_view(), name='produccion_lista'),
    path('produccion/nueva', ProduccionCreate.as_view(), name='produccion_nueva'),
    path('produccion/editar/<pk>', ProduccionUpdate.as_view(), name='produccion_editar'),
    path('tareas/', TareaList.as_view(), name='tarea_lista')
]