# Bu dosya, Django projesinin WSGI (Web Server Gateway Interface) yapılandırmasını içerir.
# Projenin bir web sunucusu (örn. Gunicorn, uWSGI) üzerinden çalıştırılmasını sağlar ve uygulama nesnesini dışa aktarır.

"""
WSGI config for sms project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/howto/deployment/wsgi/
"""
import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'sms.settings')

application = get_wsgi_application()

app = application