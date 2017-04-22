from django.views.generic.edit import CreateView
from django.views.generic import TemplateView, DetailView
from django_tables2 import tables, SingleTableView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from .models import Issue
from .tables import IssueTable

# http://www.craigderington.me/generic-list-view-with-django-tables/

class IssueIndex(LoginRequiredMixin, SingleTableView):
    model = Issue
    table_class = IssueTable
    template_name = "issue_index.html"

    def issue_number(self):
        return len(Issue.objects.all())
    
    def good_issues(self):
        return 3

    def bad_issues(self):
        return 7


class IssueCreate(LoginRequiredMixin, CreateView):
    model = Issue
    fields =  ['description', 'category', 'priority', 'issue_type', 'sf_contact', 'contract']
    template_name = "issue_form.html"
    success_url = reverse_lazy('issues:index')


class IssueDetail(LoginRequiredMixin, DetailView):
    model = Issue
    template_name = "issue_detail.html"