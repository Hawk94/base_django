from django.conf.urls import url
from .views import CustomerIndex, CustomerDetail, CustomerCreate

urlpatterns = [
    url(r'^$', CustomerIndex.as_view(), name='index'),
    url(r'add/', CustomerCreate.as_view(), name='add'),
    # url(r'^(?P<pk>[0-9]+)/$', CustomerDetail.as_view(), name='customer_detail'),
    url(r'^customer/(?P<pk>\d+)/$', CustomerDetail.as_view(), name='customer-detail'),
]
