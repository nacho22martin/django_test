from django.conf.urls import patterns, url

from catalogo import views

urlpatterns = patterns('',
    # ex: /articulo/
    # url(r'^$', views.index, name='index'),  # XXX: Por ahora no usamos esto
    # ex: /articulo/5/
    url(r'^$', views.index, name='index'),
    url(r'^(?P<vehiculo_id>\d+)/$', views.detalle, name='detalle'),
    # ex: /articulo/busqueda?marca=Ford
    url(r'^busqueda/$', views.busqueda, name='busqueda'),
    url(r'^servicios/$', views.servicios, name='servicios'),
    url(r'^about/$', views.about, name='about'),
    url(r'^detalle/$', views.detalle, name='detalle'),
)