# -*- coding: utf-8 -*-

import json

from django import forms
from django.contrib import admin

from django.core.mail import send_mail

from django.conf import settings

from django.core.exceptions import ImproperlyConfigured

from django.forms.util import flatatt

from django.utils.html import escape, format_html

from django.template.loader import render_to_string

from catalogo.models import Prestacion


class CustomPrestacionesWidget(forms.Widget):

    def render(self, name, value, attrs=None):
        if value is None:
            value = []
        else:
            value = json.loads(value)
        #import pdb;pdb.set_trace()
                
        html = "<br />"
        for prestacion_obj in Prestacion.objects.all():
            html += "<br /><h3>%s</h3><br />" % prestacion_obj.titulo
            for prestacion in prestacion_obj.prestaciones.split('\r\n'):
                if not prestacion:
                    continue
                att = {'type': "checkbox",
                       'value': prestacion,
                       'data-hidden-id': attrs['id'],}

                if prestacion in value:
                    att['checked'] = 'checked'

                html += "<input %s onchange=togglePrestacion(this) /> %s" % (flatatt(att), prestacion)
                html += "<br />"
        
        attrs['name'] = name
        attrs['type'] = 'hidden'
        html = "<input %s value=\"%s\" /> %s" % (flatatt(attrs), escape(json.dumps(value)), html)
        html = """
               <script type=\"text/javascript\" src=\"/static/js/admin.js\"></script>
               %s
               """ % html
        return format_html(html)

class VehiculoAdminForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(VehiculoAdminForm, self).__init__(*args, **kwargs)
        self.fields['prestaciones'].widget = CustomPrestacionesWidget()
        
        
class ContactForm(forms.Form):
    name = forms.CharField(label=u'Nombre', max_length=100)
    email = forms.EmailField(label=u'Email', max_length=100)
    phone = forms.CharField(label=u'Telefono', max_length=100)
    message = forms.CharField(label=u'Mensaje', widget=forms.Textarea(), max_length=500)

    def send_email(self):
        """
        Send contact form as an email to the address specified in the
        CONTACT_EMAILS setting.
        """
        from_email = self.cleaned_data['email']
        if not hasattr(settings, 'CONTACT_EMAILS'):
            raise ImproperlyConfigured("You need to specify CONTACT_EMAILS in "
                                       "your Django settings file.")
        to_emails = settings.CONTACT_EMAILS
        subject = "Email enviado desde sitio web"
        template_name = 'contact/email.txt'
        message = render_to_string(template_name, self.cleaned_data)
        
        send_mail(subject, message, from_email, to_emails)