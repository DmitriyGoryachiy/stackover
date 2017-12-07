from django.conf.urls import url
from Categories.views import CategoryDetail

urlpatterns = [
    url(r'^categorydetail/(?P<pk>\d+)$',CategoryDetail.as_view(), name = 'category_detail'),
]