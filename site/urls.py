"""zoo_site URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import include, url
from main.accounts import urls as accounts_urls
from main.customers import urls as customer_urls
from main.issues import urls as issue_urls
from django.contrib import admin
from .views import HomePage

from two_factor.gateways.twilio.urls import urlpatterns as tf_twilio_urls
from two_factor.urls import urlpatterns as tf_urls


urlpatterns = [
    url(r'^$', HomePage.as_view(), name='home'),
    url(r'^accounts/', include(accounts_urls, namespace='accounts')),
    url(r'^customers/', include(customer_urls, namespace='customers')),
    url(r'^issues/', include(issue_urls, namespace='issues')),
    url(r'^admin/', admin.site.urls),
    
    url(r'', include('two_factor.urls', 'two_factor')),
]
