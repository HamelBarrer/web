from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models.signals import post_save
from django.dispatch import receiver


# Create your models here.


class Usuario(AbstractUser):
    is_administrador = models.BooleanField(default=False)
    is_satelite = models.BooleanField(default=False)

    def get_administrador(self):
        administrador = None
        if hasattr(self, 'administrador'):
            administrador = self.administrador
        return administrador

    def get_satelite(self):
        satelite = None
        if hasattr(self, 'satelite'):
            satelite = self.satelite
        return satelite

    def __str__(self):
        return '%s %s' % (self.first_name, self.last_name)

    class Meta:
        db_table = 'auth_user'


class Administrador(models.Model):
    usuario = models.OneToOneField(Usuario, on_delete=models.CASCADE)
    imagen = models.ImageField(null=True, blank=True)
    razon_social = models.CharField(max_length=30)


class Satelite(models.Model):
    usuario = models.OneToOneField(Usuario, on_delete=models.CASCADE)
    imagen = models.ImageField(null=True, blank=True)
    nivel_acadademico = models.CharField(max_length=30)

    def __str__(self):
        return str(self.usuario)


@receiver(post_save, sender=Usuario)
def asignar_rol(sender, instance, **kwargs):
    if kwargs.get('created', False):
        if instance.is_administrador:
            Administrador.objects.get_or_create(usuario=instance)
        elif instance.is_satelite:
            Satelite.objects.get_or_create(usuario=instance)


class UsuarioExtra(models.Model):
    primer_nombre = models.CharField(max_length=30)
    segundo_nombre = models.CharField(max_length=30)
    primer_apellido = models.CharField(max_length=30)
    segundo_apellido = models.CharField(max_length=30)
    correo = models.EmailField()
    telefono = models.CharField(max_length=10)
    estado = models.BooleanField(default=True)

    def __str__(self):
        return '%s %s %s %s' % (self.primer_nombre, self.segundo_nombre, self.primer_apellido, self.segundo_apellido)

    class Meta:
        abstract: True


class Proveedor(UsuarioExtra):
    razon_social = models.CharField(max_length=30)


class Cliente(UsuarioExtra):
    razon_social = models.CharField(max_length=30)
