import django_tables2 as tables
from django_tables2.utils import A
from .models import Customer


class CustomerTable(tables.Table):

    class Meta:
        model = Customer
        fields = ('name', 'initial_start_date')
        attrs = {"class": "table-striped table-bordered"}