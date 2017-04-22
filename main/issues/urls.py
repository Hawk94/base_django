from django.conf.urls import url
from .views import IssueIndex, IssueCreate, IssueDetail

urlpatterns = [
    url(r'^$', IssueIndex.as_view(), name='index'),
    url(r'add/', IssueCreate.as_view(), name='add'),
    url(r'^issue/(?P<pk>\d+)/$', IssueDetail.as_view(), name='issue-detail'),
]
