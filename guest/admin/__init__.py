"""Admin for guest app."""
from django.contrib import admin
from guest.models import Guest


admin.site.register(Guest)
