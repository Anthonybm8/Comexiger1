import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "COMEXIGER.settings")

django.setup()

from django.core.management import call_command

call_command("makemigrations")
call_command("migrate")
