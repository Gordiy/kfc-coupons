"""An object that describes Guests of KFC.."""
from django.db import models


class Guest(models.Model):
    """An object that describes Guests of KFC."""
    unique_id = models.CharField(unique=True, max_length=150, blank=True, null=True)
    created_at = models.DateField(auto_now_add=True)

    def __str__(self) -> str:
        return f"{self.unique_id} - {self.created_at}"
