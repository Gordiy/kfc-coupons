"""A serializer that works with the coupon model."""
from rest_framework import serializers

from coupon.models import Coupon


class CouponSerializer(serializers.ModelSerializer):
    """A serializer that works with the coupon model."""
    guest_unique_id = serializers.SerializerMethodField()

    class Meta:
        """Meta data."""
        model = Coupon
        fields = ['number', 'guest_unique_id']

    def get_guest_unique_id(self, coupon: Coupon) -> str:
        """Get guest unique id."""
        return coupon.guest.unique_id
