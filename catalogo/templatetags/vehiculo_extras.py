from django import template

from catalogo.models import Prestacion

register = template.Library()

@register.filter(name='getimages')
def getimages(vehiculo):
    image_prefix = "imagen_"
    images = []
    for i in range(1,11):
        field_id = "%s%s"%(image_prefix,i)
        image = getattr(vehiculo, field_id, False)
        if image and not image.name == u'':
          images.append(image)
    return images


@register.filter(name='getspecs')
def getspecs(vehiculo):
    specs = {}
    for spec in Prestacion.objects.all():
        for entry in spec.prestaciones.split("\r\n"):
            if entry in vehiculo.prestaciones:
                cur_specs = specs.get(spec.titulo, [])
                if entry not in cur_specs:
                    cur_specs.append(entry)
                    specs[spec.titulo] = cur_specs
    return sorted(specs.iteritems())