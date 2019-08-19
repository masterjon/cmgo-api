"""
WSGI config for cmgo project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application


#os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'cmgo.settings')

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'cmgo.settings.production')
#>>>>>>> 8b50b85abed49d24af751f750fba8393fda24876

application = get_wsgi_application()
