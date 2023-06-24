"""The viewset to retrieve coupon."""
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK
from rest_framework.views import APIView

from coupon.serializers import CouponSerializer
from coupon.services import CouponsService


class RetrieveCouponsAPIView(APIView):
    """The viewset to retrieve coupon."""
    def get(self, request: Request) -> Response:
        """Create and retrieve coupon."""

        unique_id = request.query_params.get('unique_id', '')

        coupon = CouponsService.generate_coupon(unique_id)

        serializer = CouponSerializer(coupon)

        return Response(serializer.data, status=HTTP_200_OK)
