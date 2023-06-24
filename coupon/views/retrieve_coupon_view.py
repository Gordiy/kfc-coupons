"""The viewset to retrieve coupon."""
from rest_framework.exceptions import ValidationError
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST
from rest_framework.views import APIView

from coupon.models import Coupon
from coupon.serializers import CouponSerializer
from coupon.utils import generate_unique_coupon_number
from guest.models import Guest


class RetrieveCouponsAPIView(APIView):
    """The viewset to retrieve coupon."""
    def get(self, request: Request) -> Response:
        """Create and retrieve coupon."""
        number = generate_unique_coupon_number()

        unique_id = request.query_params.get('unique_id', '')

        if not unique_id:
            raise ValidationError(detail='unique_id can not be blank.', code=HTTP_400_BAD_REQUEST)

        try:
            guest = Guest.objects.create(unique_id=unique_id)
        except Exception:
            raise ValidationError(detail='The user already had a coupon.', code=HTTP_400_BAD_REQUEST)

        coupon = Coupon.objects.create(number=number, guest=guest)
        coupon.save()

        serializer = CouponSerializer(coupon)

        return Response(serializer.data, status=HTTP_200_OK)
