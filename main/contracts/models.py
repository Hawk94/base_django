from django.db import models
from django.utils import timezone

from ..customers.models import Customer


class Commission(models.Model):

    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)

    rate = models.PositiveIntegerField(default=0)
    discount = models.PositiveIntegerField(default=0)


class Contact(models.Model):

    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)

    name = models.CharField(max_length=50)


class AccountManager(models.Model):

    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)
    
    hurdle_period = models.PositiveIntegerField(default=0)  # Stored as an integer of months
    hurdle = models.PositiveIntegerField(default=0)
    contact = models.ForeignKey('Contact')


class Partner(models.Model):

    PARTNER_TYPES = (
        ('TE', 'Technical'),
        ('SE', 'Services'),
        ('CT', 'Consultant'),
    )

    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)

    contact = models.ForeignKey('Contact')


class Contract(models.Model):

    TERMINATION_CLAUSES = (
        ('OM', 'One Month'),
        ('OQ', 'One Quarter'),
        ('OY', 'One Year'),
    )

    LANGUAGES = (
        ('EN', 'English'),
        ('AM', 'American'),
        ('SP', 'Spanish'),
        ('PO', 'Portugese'),
        ('CH', 'Chinese'),
    )

    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)

    is_customer_success = models.BooleanField(default=False)
    renewable_income =  models.DecimalField(max_digits=8, decimal_places=2)
    non_renewable_income = models.DecimalField(max_digits=8, decimal_places=2)
    currency = models.CharField(max_length=3)
    start_date = models.DateTimeField()
    renewal_date = models.DateTimeField()
    termination_clause = models.CharField(max_length=2, choices=TERMINATION_CLAUSES)
    term = models.DurationField()
    plants = models.PositiveIntegerField()
    catalogues = models.PositiveIntegerField()
    banding = models.PositiveIntegerField()
    languages = models.CharField(max_length=2, choices=LANGUAGES)
    is_active = models.BooleanField(default=False)
    

    customer = models.ForeignKey(Customer)
    partner = models.ForeignKey(Partner)
    account_manager = models.ForeignKey(AccountManager)
    key_user = models.ForeignKey(Contact, related_name='key_user')
    project_sponsor = models.ForeignKey(Contact, related_name='project_sponsor')
    executive_contact = models.ForeignKey(Contact, related_name='executive_contact')
    partner_commission = models.OneToOneField(Commission, related_name='partner_commission')
    account_manager_commission = models.OneToOneField(Commission, related_name='account_manager_commission')
