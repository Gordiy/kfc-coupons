"""Generate unique coupon number."""
import random

from coupon.models import Coupon


def generate_unique_coupon_number() -> int:
    """Generate unique coupon number."""
    while True:
        random_value = random.randint(1000000, 1100000)
        try:
            # Check if a Coupon object with the same number exists
            Coupon.objects.get(number=random_value)
        except Coupon.DoesNotExist:
            # If no Coupon object exists with the same number, return the random value
            return random_value
