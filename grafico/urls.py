from django.urls import path
from .views import grafico
urlpatterns = [
    path('graficos/', grafico, name='grafico'),
]