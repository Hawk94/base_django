from django.views.generic.edit import CreateView
from django.views.generic import TemplateView, DetailView
from django_tables2 import tables, SingleTableView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from .models import Customer
from .tables import CustomerTable

# http://www.craigderington.me/generic-list-view-with-django-tables/

class CustomerIndex(LoginRequiredMixin, SingleTableView):
    model = Customer
    table_class = CustomerTable
    template_name = "customer_index.html"
    
    def customer_number(self):
        return len(Customer.objects.all())
    
    def health_score(self):
        return '60%'

    def renewals(self):
        return 4


class CustomerCreate(LoginRequiredMixin, CreateView):
    model = Customer
    fields = ['name', 'initial_start_date']
    template_name = "customer_form.html"
    success_url = reverse_lazy('customers:index')


class CustomerDetail(LoginRequiredMixin, DetailView):
    model = Customer
    template_name = "customer_detail.html"