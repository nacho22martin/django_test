# -*- coding: utf-8 -*-

from django.db import models
from django.db.models.signals import post_save


class Vehiculo(models.Model):
    titulo = models.CharField(u'Título', max_length=250)
    titulo_destacado = models.CharField(u'Título de destacado', max_length=250, blank=True)
    es_destacado = models.BooleanField(u'Destacado')

    # Campos sobre el vehiculo
    marca = models.ForeignKey('Marca')
    modelo = models.CharField(u'Modelo', max_length=27)  # TODO: FK?
    segmento = models.CharField(u'Segmento', max_length=50)
    precio = models.DecimalField(u'Precio', max_digits=9, decimal_places=2)
    kilometros = models.IntegerField(u'Kilómetros')
    color = models.CharField(u'Color', max_length=30)
    ano = models.IntegerField(u'Año')
    combustible = models.ForeignKey('Combustible')

    # Titular
    titular = models.ForeignKey('Titular')

    # Campos sobre el pago y la financiacion
    anticipo = models.DecimalField(u'Anticipo', max_digits=9, decimal_places=2,
                                   null=True, blank=True)
    forma_pago = models.CharField(u'Forma de pago', max_length=100, blank=True)  # TODO: FK
    
    # Campos opcionales en caso que el auto se encuentre en otro domicilio
    provincia = models.CharField(u'Provincia', max_length=25, blank=True)  # TODO: FK
    partido = models.CharField(u'Partido', max_length=25, blank=True)  # TODO: FK
    localidad = models.CharField(u'Localidad', max_length=25, blank=True)  # TODO: FK
    direccion = models.CharField(u'Dirección', max_length=150, blank=True)
    direccion2 = models.CharField(u'Dirección (datos adicionales)', max_length=150, blank=True)
    
    # Imagenes
    imagen_catalogo = models.ImageField(u'Imagen del catálogo', upload_to='fotos/%Y/%m/%d', blank=True)
    imagen_1 = models.ImageField(u'Imagen adicional 1', upload_to='fotos/%Y/%m/%d', blank=True)
    imagen_2 = models.ImageField(u'Imagen adicional 2', upload_to='fotos/%Y/%m/%d', blank=True)
    imagen_3 = models.ImageField(u'Imagen adicional 3', upload_to='fotos/%Y/%m/%d', blank=True)
    imagen_4 = models.ImageField(u'Imagen adicional 4', upload_to='fotos/%Y/%m/%d', blank=True)
    imagen_5 = models.ImageField(u'Imagen adicional 5', upload_to='fotos/%Y/%m/%d', blank=True)
    imagen_6 = models.ImageField(u'Imagen adicional 6', upload_to='fotos/%Y/%m/%d', blank=True)
    imagen_7 = models.ImageField(u'Imagen adicional 7', upload_to='fotos/%Y/%m/%d', blank=True)
    imagen_8 = models.ImageField(u'Imagen adicional 8', upload_to='fotos/%Y/%m/%d', blank=True)
    imagen_9 = models.ImageField(u'Imagen adicional 9', upload_to='fotos/%Y/%m/%d', blank=True)
    imagen_10 = models.ImageField(u'Imagen adicional 10', upload_to='fotos/%Y/%m/%d', blank=True)

    prestaciones = models.TextField(u'Prestaciones', blank=True)
    
    def __unicode__(self):
        return self.titulo

    class Meta:
        verbose_name_plural = u'Vehículos'


def solo_un_destacado(sender, instance, signal, *args, **kwargs):
    if instance.es_destacado:
        # Significa que el vehiculo que se esta guardando, fue seleccionado
        # como destacado, tenemos que sacarle el destacado al otro vehiculo
        # que lo pueda tener (si hay alguno)
        destacados = Vehiculo.objects.filter(es_destacado=True)
        for vehiculo in destacados:
            if not vehiculo == instance:
                vehiculo.es_destacado = False
                vehiculo.save()

post_save.connect(solo_un_destacado, sender=Vehiculo)


class Titular(models.Model):
    nombre = models.CharField(u'Nombre', max_length=250)
    email = models.EmailField(u'E-Mail', max_length=75, blank=True)
    dni = models.IntegerField(u'DNI', null=True, blank=True)
    telefono = models.CharField(u'Teléfono', max_length=15)
    telefono2 = models.CharField(u'Teléfono secundario', max_length=15, blank=True)
    provincia = models.CharField(u'Provincia', max_length=25)  # TODO: FK
    partido = models.CharField(u'Partido', max_length=25)  # TODO: FK
    localidad = models.CharField(u'Localidad', max_length=25)  # TODO: FK
    direccion = models.CharField(u'Dirección', max_length=150)
    direccion2 = models.CharField(u'Dirección (datos adicionales)', max_length=150, blank=True)
    notas = models.TextField(u'Notas', blank=True)

    def __unicode__(self):
        return "%s (%s) %s " % (self.nombre, self.telefono, self.email)

    class Meta:
        verbose_name_plural = u'Titulares'


class Combustible(models.Model):
    titulo = models.CharField(u'Titulo', max_length=200)

    def __unicode__(self):
        return "%s" % self.titulo

    class Meta:
        verbose_name_plural = u'Combustibles'


class Marca(models.Model):
    titulo = models.CharField(u'Titulo', max_length=200)

    def __unicode__(self):
        return "%s" % self.titulo

    class Meta:
        verbose_name_plural = u'Marcas'


class Prestacion(models.Model):
    titulo = models.CharField(u'Titulo', max_length=200)
    prestaciones = models.TextField(u'Prestaciones (Una por linea)')

    def __unicode__(self):
        return "%s" % self.titulo

    class Meta:
        verbose_name_plural = u'Prestaciones'