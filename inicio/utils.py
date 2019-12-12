from functools import wraps
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required

def custom_login_required(view_func):
    @wraps(view_func)
    def wrapped_view(request, *args, **kwargs):
        usuario = request.usuario
        LOGIN_URL = '/'
        user_groups = user.groups.values_list('name', flat=True)
        if 'Satelite' in user_groups:
            LOGIN_URL = 'usuario:usuario_lista'
        elif usuario.is_admin:
            LOGIN_URL = '/admin'
        else:
            LOGIN_URL = '/'
        if usuario.is_authenticated:
            return view_func(request, *args, **kwargs)
        return redirect(LOGIN_URL)
    return wrapped_view