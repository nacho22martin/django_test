# -*- coding: utf-8 -*-

from django.shortcuts import render, get_object_or_404

from quix.django.contact.views import ContactView as BaseContactView

from catalogo.models import Vehiculo
from catalogo.models import Marca
from catalogo.models import Combustible



def index(request):
    if request.GET:
        results = Vehiculo.objects.filter(**request.GET.dict())
    else:
        results = Vehiculo.objects.all().order_by('marca')  # XXX: Por ahora ordenamos por marca.
    destacado = Vehiculo.objects.filter(es_destacado=True)

    marcas = [(i.id, i.titulo) for i in Marca.objects.all()]
    modelos = set([i.modelo for i in Vehiculo.objects.all()])  # XXX: Buscar como pedir objetos unicos
    return render(request, 'index.html', {'results': results,
                                          'destacado': destacado,
                                          'marcas': marcas,
                                          'modelos': modelos,})


def detalle(request, vehiculo_id):
    vehiculo = get_object_or_404(Vehiculo, pk=vehiculo_id)
    return render(request, 'vehiculo/detalle.html', {'vehiculo': vehiculo})


def busqueda(request):
    if request.GET:
        data = {}
        for key, value in request.GET.items():
            if value == u'0':
                continue

            data[key] = value
        results = Vehiculo.objects.filter(**data)
    else:
        results = Vehiculo.objects.all().order_by('marca')  # XXX: Por ahora ordenamos por marca.
        
    
    marcas = [(i.id, i.titulo) for i in Marca.objects.all()]
    vehiculos = Vehiculo.objects.all()
    modelos = set([i.modelo for i in vehiculos])
    anos = set([i.ano for i in vehiculos])
    kms = set([i.kilometros for i in vehiculos])
    colores = set([i.color for i in vehiculos])
    combustibles = [(i.id, i.titulo) for i in Combustible.objects.all()]

    return render(request, 'vehiculo/busqueda.html',
                  {'results': results,
                   'marcas': marcas,
                   'modelos': modelos,
                   'anos': anos,
                   'kms': kms,
                   'colores': colores,
                   'combustibles':combustibles,})

def about(request):   
    return render(request, 'vehiculo/about.html')

def servicios(request):   
    return render(request, 'vehiculo/servicios.html')

class ContactView(BaseContactView):

    def get_initial(self):
        initial = super(ContactView, self).get_initial()
        if 'vehiculo' in self.request.GET:
            try:
                v_id = int(self.request.GET.get('vehiculo'))
            except ValueError:
                v_id = 0
            
            if v_id != 0:
                vehiculos = Vehiculo.objects.filter(id=v_id)
                
                if vehiculos:
                    vehiculo = vehiculos[0]
                    
                    msg = (u"ID de vehiculo: %s\r\n"
                           u"Marca: %s\r\n"
                           u"Modelo: %s\r\n"
                           u"Segmento: %s\r\n"
                           u"Precio: %s\r\n"
                           u"Año: %s\r\n"
                           u"Color: %s\r\n"
                           u"KMs: %s\r\n\r\n" % (vehiculo.id,
                                                 vehiculo.marca.titulo,
                                                 vehiculo.modelo,
                                                 vehiculo.segmento,
                                                 vehiculo.precio,
                                                 vehiculo.ano,
                                                 vehiculo.color,
                                                 vehiculo.kilometros))
                    
                    initial['message'] = msg
        return initial
