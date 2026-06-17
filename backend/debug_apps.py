import os
import django
from django.conf import settings

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

from django.apps import apps
for app_config in apps.get_app_configs():
    if app_config.name.startswith('apps.'):
        print(f"App: {app_config.name}, Label: {app_config.label}")
        for model in app_config.get_models():
            print(f"  Model: {model.__name__}")
