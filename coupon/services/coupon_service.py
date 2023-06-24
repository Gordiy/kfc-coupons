"""Coupon service."""
from rest_framework.exceptions import ValidationError
from rest_framework.status import HTTP_400_BAD_REQUEST

from coupon.models import Coupon


class CouponsService:
    """Coupon service."""
    @staticmethod
    def remove_coupon(number: str) -> None or ValidationError:
        """
        Remove coupon from db.
        
        :number: coupon number.
        :return:
        :raises ValidationError: if coupon with current number does not exist.
        """
        try:
            obj = Coupon.objects.get(number=number)
            obj.delete()
        except Coupon.DoesNotExist:
            raise ValidationError(detail=f'Coupon with number {number} does not exists.', code=HTTP_400_BAD_REQUEST)
