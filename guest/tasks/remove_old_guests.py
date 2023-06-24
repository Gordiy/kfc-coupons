"""Remove guests that stored in database more than one week."""
from datetime import datetime, timedelta

from celery import shared_task

from guest.models import Guest


@shared_task
def remove_old_guests():
    """Remove guests that stored in database more than one week."""
    one_week_ago = datetime.now().date() - timedelta(days=7)
    Guest.objects.filter(created_at__lt=one_week_ago).delete()
