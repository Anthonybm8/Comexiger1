import os
import sys

# Ruta del proyecto
PROJECT_PATH = '/home/damisoft/comexiger.damisoft-ec.com'
if PROJECT_PATH not in sys.path:
    sys.path.insert(0, PROJECT_PATH)

# Settings de Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'COMEXIGER.settings')

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
