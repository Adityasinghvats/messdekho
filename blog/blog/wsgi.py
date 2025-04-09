"""
WSGI config for blog project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.1/howto/deployment/wsgi/
"""

import os
from django.core.wsgi import get_wsgi_application

# Add this block to run migrations on startup
from django.core.management import call_command
try:
    call_command('migrate')
except Exception as e:
    print(f"Error running migrations: {e}")

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'blog.settings')

application = get_wsgi_application()
