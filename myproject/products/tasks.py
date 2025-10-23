# products/tasks.py
import time
import logging
from celery import shared_task
from celery.exceptions import SoftTimeLimitExceeded
from datetime import date
from .models import Product

logger = logging.getLogger(__name__)

@shared_task(bind=True, soft_time_limit=10, time_limit=15)
def deactivate_expired_products(self):
    try:
        expired_products = Product.objects.filter(
            expiration_date__lte=date.today(),
            is_active=True
        )
        count = expired_products.count()
        for product in expired_products:
            time.sleep(30)
            product.is_active = False
            product.save()
        message = f"{count} products were marked inactive."
        print(message)
        logger.info(message)
        return message
    except SoftTimeLimitExceeded:
        message = "Task soft time limit exceeded! Exiting gracefully."
        print(message)
        logger.warning(message)
        return message






