from django.urls import path
from coupon.views import RetrieveCouponsAPIView, RemoveCouponsAPIView

urlpatterns = [
    path('remove/<int:coupon_number>/', RemoveCouponsAPIView.as_view(), name='remove-coupon'),
    path('retrieve/', RetrieveCouponsAPIView.as_view(), name='retrieve-coupon'),
]
