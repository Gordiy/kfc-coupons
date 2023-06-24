"""An object that describes Guests of KFC.."""
from django.db import models


class Guest(models.Model):
    """An object that describes Guests of KFC."""
    unique_id = models.CharField(unique=True, max_length=150)
