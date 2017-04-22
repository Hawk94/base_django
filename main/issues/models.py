from django.db import models
from django.utils import timezone

from ..contracts.models import Contact, Contract


class Issue(models.Model):
    
    PRIORITIES = (
        ('R', 'Red'),
        ('A', 'Amber'),
        ('G', 'Green'),
    )
    
    ISSUE_TYPE = (
        ('PO', 'Positive'),
        ('NE', 'Negative'),
    )

    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)

    description = models.CharField(max_length=1000)
    priority = models.CharField(max_length=1, choices=PRIORITIES)
    category = models.CharField(max_length=50)
    issue_type = models.CharField(max_length=1, choices=PRIORITIES)

    sf_contact = models.ForeignKey(Contact)
    contract = models.ForeignKey(Contract)