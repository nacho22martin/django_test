# Django settings for augustorubio project.
from settings import *

DEBUG = False
TEMPLATE_DEBUG = DEBUG

ADMINS = (
    ('Ignacio Martin', 'nacho22martin@gmail.com'),
)

MANAGERS = ADMINS

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'augustorubio',
        'USER': 'augustorubio',
        'PASSWORD': 'super5ec#rep455w0rD!!',
        'HOST': '',
        'PORT': '',
    }
}

# Absolute filesystem path to the directory that will hold user-uploaded files.
# Example: "/var/www/example.com/media/"
MEDIA_ROOT = '/var/www/augusto/media/'

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash.
# Examples: "http://example.com/media/", "http://media.example.com/"
MEDIA_URL = 'armweb.com/media/'

# Hosts/domain names that are valid for this site; required if DEBUG is False
# See https://docs.djangoproject.com/en/1.5/ref/settings/#allowed-hosts
ALLOWED_HOSTS = ['*']

# Make this unique, and don't share it with anybody.
SECRET_KEY = 'zb0@7cmp4!rn0ac0bw=#d^(-s4@o8_o8qtg$3mg(^12%(9)5^f'

#Contact Form
CONTACT_EMAILS = ('nacho22martin@gmail.com', "ignacio@smasesores.com.ar")

EMAIL_HOST = u"smtp.gmail.com"
EMAIL_PORT = 587

EMAIL_HOST_USER = u"" 
EMAIL_HOST_PASSWORD = u""

EMAIL_USE_TLS = True
EMAIL_USE_SSL = True

