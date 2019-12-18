from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.views import generic
from .models import Contacto
from .forms import ContactoForm


# Create your views here.
class Index(generic.CreateView):
    model = Contacto
    context_object_name = 'obj'
    template_name = 'index.html'
    form_class = ContactoForm
    success_url = reverse_lazy('inicio:inicio')


class SinPrivilegios(LoginRequiredMixin, PermissionRequiredMixin):
    login_url = 'base:login'
    raise_exception = False
    redirect_field_name = 'redirect_to'

    def handle_no_permission(self):
        from django.contrib.auth.models import AnonymousUser
        if not self.request.user == AnonymousUser():
            self.login_url = 'base:sin_privilegios'
        return HttpResponseRedirect(reverse_lazy(self.login_url))


class InicioSinPrivilegios(LoginRequiredMixin, generic.TemplateView):
    login_url = 'base:login'
    template_name = 'bases/sin_privilegios.html'
