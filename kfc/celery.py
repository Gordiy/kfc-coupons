# celery.py
import os

from celery import Celery

# Set the default Django settings module
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'kfc.settings')

# Create an instance of Celery
app = Celery('kfc')

# Load configuration from Django settings
app.config_from_object('django.conf:settings', namespace='CELERY')

# Discover tasks in the Django app
app.autodiscover_tasks()
