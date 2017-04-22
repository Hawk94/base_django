from django.forms import ModelForm
from .models import Customer


class CustomerForm(ModelForm):
    class Meta:
        model = Customer
        fields = ['name', 'initial_start_date']