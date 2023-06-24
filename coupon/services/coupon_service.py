"""Coupon service."""
from rest_framework.exceptions import ValidationError
from rest_framework.status import HTTP_400_BAD_REQUEST

from coupon.models import Coupon
from coupon.utils import generate_unique_coupon_number
from guest.models import Guest


class CouponsService:
    """Coupon service."""
    @staticmethod
    def remove_coupon(number: str) -> None or ValidationError:
        """
        Remove coupon from db.
        
        :param number: coupon number.
        :return:
        :raises ValidationError: if coupon with current number does not exist.
        """
        try:
            obj = Coupon.objects.get(number=number)
            obj.delete()
        except Coupon.DoesNotExist:
            raise ValidationError(detail=f'Coupon with number {number} does not exists.', code=HTTP_400_BAD_REQUEST)
        
    @staticmethod
    def generate_coupon(unique_id: str) -> Coupon or ValidationError:
        """
        Generate unique coupon.

        :param unique_id: unique guest identificator.
        :return: an instance of created Coupon.
        :raises ValidationError: if unique_id is blank.
        :raises ValidationError: if user already had a coupon.
        """
        number = generate_unique_coupon_number()

        if not unique_id:
            raise ValidationError(detail='unique_id can not be blank.', code=HTTP_400_BAD_REQUEST)

        try:
            guest = Guest.objects.create(unique_id=unique_id)
        except Exception:
            raise ValidationError(detail='The user already had a coupon.', code=HTTP_400_BAD_REQUEST)

        coupon = Coupon.objects.create(number=number, guest=guest)
        coupon.save()

        return coupon
