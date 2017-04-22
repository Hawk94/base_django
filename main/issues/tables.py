import django_tables2 as tables
from django_tables2.utils import A
from .models import Issue


class IssueTable(tables.Table):

    class Meta:
        model = Issue
        fields = ('category', 'priority')
        attrs = {"class": "table-striped table-bordered"}