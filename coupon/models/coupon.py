"""An object that describes coupons for KFC guests."""
from django.db import models
from guest.models import Guest


class Coupon(models.Model):
    """An object that describes coupons for KFC guests."""
    number = models.BigIntegerField(unique=True, null=False, blank=False)
    guest = models.ForeignKey(Guest, on_delete=models.CASCADE)
