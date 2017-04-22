from django.db import models
from django.utils import timezone


class Product(models.Model):
    
    PRODUCT_TYPES = (
        ('GA', 'Gatekeeper'),
        ('IN', 'Insight'),
        ('MA', 'Masterpiece'),
        ('FI', 'Finder'),
        ('WO', 'Workbench'),
    )

    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)

    product_type = models.CharField(max_length=2, choices=PRODUCT_TYPES)