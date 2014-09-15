from django.contrib import admin
from catalogo.models import Titular
from catalogo.models import Vehiculo
from catalogo.models import Combustible
from catalogo.models import Marca
from catalogo.models import Prestacion

from forms import VehiculoAdminForm

class VehiculoAdmin(admin.ModelAdmin):
    form = VehiculoAdminForm
    fieldsets = [
        (None,               {'fields': ['titulo',
                                         'titulo_destacado',
                                         'es_destacado',
                                         'titular', 
                                         'imagen_catalogo', 
                                         'imagen_1', 
                                         'imagen_2', 
                                         'imagen_3',
                                         'imagen_4', 
                                         'imagen_5', 
                                         'imagen_6',
                                         'imagen_7', 
                                         'imagen_8', 
                                         'imagen_9', 
                                         'imagen_10']}),
        ('Vehiculo', {'fields': ['marca',
                                 'modelo',
                                 'segmento',
                                 'precio',
                                 'kilometros',
                                 'color',
                                 'ano',
                                 'combustible',
                                 'prestaciones']}),
        ('Pago', {'fields': ['anticipo', 'forma_pago']}),
        # XXX: Estos campos no son necesarios, pero dejo comentado por las dudas
        #      para el futuro
        #('Direccion (en caso que no sea la misma que la del titular)',
            #{'fields': ['provincia',
                        #'partido',
                        #'localidad',
                        #'direccion',
                        #'direccion2']}),
        
    ]


admin.site.register(Titular)
admin.site.register(Vehiculo, VehiculoAdmin)
admin.site.register(Combustible)
admin.site.register(Marca)
admin.site.register(Prestacion)
