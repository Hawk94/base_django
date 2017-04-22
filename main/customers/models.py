from django.db import models
from django.urls import reverse
from django.utils import timezone

from ..products.models import Product


class Customer(models.Model):

    CUSTOMER_STATUS = (
        ('LE', 'Lead'),
        ('OB', 'Onboarding'),
        ('KO', 'Kick-off'),
        ('GL', 'Go Live'),
        ('SU', 'Support'),
        ('BU', 'Business as Usual'),
    )

    CONSULTANTS = (
        ('PH', 'Peter Hardy'),
        ('PS', 'Paul Shoesmith'),
    )

    PROJECT_MANAGERS = (
        ('ES', 'Esther Saez'),
        ('IG', 'Isabel Giraldo'),
        ('JM', 'Jonathan Melunsky'),
        ('MR', 'Matthew Rees'),
        ('OE', 'Olola Elias'),
    )


    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)

    name = models.CharField(max_length=50)
    gatekeeper_integration = models.BooleanField(default=False)
    status = models.CharField(max_length=2, choices=CUSTOMER_STATUS)
    consultant = models.CharField(max_length=2, choices=CONSULTANTS)
    project_manager = models.CharField(max_length=2, choices=PROJECT_MANAGERS)
    on_sell = models.BooleanField(default=False)
    initial_start_date = models.DateTimeField()
    
    product = models.ManyToManyField(Product)


    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('customer.views.details', args=[str(self.id)])

