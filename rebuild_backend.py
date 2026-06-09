import os

def write(path, content):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, 'w') as f:
        f.write(content.strip())

write('backend/mch_backend/settings.py', """
import os
from pathlib import Path
from datetime import timedelta

BASE_DIR = Path(__file__).resolve().parent.parent
SECRET_KEY = 'django-insecure-key'
DEBUG = True
ALLOWED_HOSTS = ['*']

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'rest_framework_simplejwt',
    'corsheaders',
    'apps.authentication',
    'apps.mothers',
    'apps.children',
    'apps.appointments',
    'apps.vaccinations',
    'apps.notifications',
    'apps.analytics',
    'apps.facilities',
    'apps.ai',
]

MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'mch_backend.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

DATABASES = {'default': {'ENGINE': 'django.db.backends.sqlite3', 'NAME': str(BASE_DIR / 'db.sqlite3')}}
AUTH_USER_MODEL = 'authentication.User'
REST_FRAMEWORK = {'DEFAULT_AUTHENTICATION_CLASSES': ('rest_framework_simplejwt.authentication.JWTAuthentication',)}
STATIC_URL = 'static/'
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
""")

write('backend/mch_backend/urls.py', """
from django.contrib import admin
from django.urls import path, include
urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/auth/', include('apps.authentication.urls')),
    path('api/mothers/', include('apps.mothers.urls')),
    path('api/children/', include('apps.children.urls')),
    path('api/appointments/', include('apps.appointments.urls')),
    path('api/vaccinations/', include('apps.vaccinations.urls')),
    path('api/facilities/', include('apps.facilities.urls')),
    path('api/ai/', include('apps.ai.urls')),
]
""")

apps = ['authentication', 'mothers', 'children', 'appointments', 'vaccinations', 'notifications', 'analytics', 'facilities', 'ai']
for app in apps:
    write(f'backend/apps/{app}/apps.py', f'''
from django.apps import AppConfig
class {app.capitalize()}Config(AppConfig):
    name = "apps.{app}"
    label = "{app}"
''')
    write(f'backend/apps/{app}/__init__.py', '')
    write(f'backend/apps/{app}/migrations/__init__.py', '')

write('backend/apps/authentication/models.py', """
from django.contrib.auth.models import AbstractUser
from django.db import models
class User(AbstractUser):
    class Role(models.TextChoices):
        MOTHER = 'MOTHER', 'Mother'
        NURSE = 'NURSE', 'Nurse'
        DOCTOR = 'DOCTOR', 'Doctor'
        CHW = 'CHW', 'Community Health Worker'
        ADMIN = 'ADMIN', 'Administrator'
    role = models.CharField(max_length=20, choices=Role.choices, default=Role.MOTHER)
    phone_number = models.CharField(max_length=15, unique=True, null=True, blank=True)
    must_change_password = models.BooleanField(default=True)
""")

write('backend/apps/authentication/urls.py', "from django.urls import path\\nurlpatterns = []")
write('backend/apps/mothers/models.py', "from django.db import models")
write('backend/apps/mothers/urls.py', "from django.urls import path\\nurlpatterns = []")
write('backend/apps/children/models.py', "from django.db import models")
write('backend/apps/children/urls.py', "from django.urls import path\\nurlpatterns = []")
write('backend/apps/appointments/models.py', "from django.db import models")
write('backend/apps/appointments/urls.py', "from django.urls import path\\nurlpatterns = []")
write('backend/apps/vaccinations/models.py', "from django.db import models")
write('backend/apps/vaccinations/urls.py', "from django.urls import path\\nurlpatterns = []")
write('backend/apps/facilities/models.py', "from django.db import models")
write('backend/apps/facilities/urls.py', "from django.urls import path\\nurlpatterns = []")
write('backend/apps/ai/models.py', "from django.db import models")
write('backend/apps/ai/urls.py', "from django.urls import path\\nurlpatterns = []")
write('backend/apps/analytics/models.py', "from django.db import models")
write('backend/apps/notifications/models.py', "from django.db import models")

write('backend/manage.py', """
import os
import sys
def main():
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mch_backend.settings')
    from django.core.management import execute_from_command_line
    execute_from_command_line(sys.argv)
if __name__ == '__main__':
    main()
""")
