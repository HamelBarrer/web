from django.urls import path
from django.contrib.auth import views as auth_views
from .views import (
    Index,
    InicioSinPrivilegios,
)

urlpatterns = [
    path('', Index.as_view(), name='inicio'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'),
         name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='bases/login.html'),
         name='logout'),
    path('sin_privilegios/', InicioSinPrivilegios.as_view(), name='sin_privilegios'),
]