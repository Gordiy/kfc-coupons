"""The viewset to remove coupons."""
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.status import HTTP_204_NO_CONTENT
from rest_framework.views import APIView

from coupon.services import CouponsService


class RemoveCouponsAPIView(APIView):
    """The viewset to remove coupons."""
    def delete(self, request: Request, coupon_number: str) -> Response:
        """Remove coupons from DB."""
        CouponsService.remove_coupon(coupon_number)

        return Response(status=HTTP_204_NO_CONTENT)
