from django.conf import settings
from django.conf.urls import patterns, include, url
from django.conf.urls.static import static

from catalogo.views import ContactView
from django.views.generic import TemplateView

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'augustorubio.views.home', name='home'),
    # url(r'^augustorubio/', include('augustorubio.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    url(r'^vehiculo/', include('catalogo.urls')),
    url(r'^contact/', ContactView.as_view()),
    url(r'^contact-success/$', TemplateView.as_view(template_name="contact/success.html"),
        name="contact-success"),
) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
