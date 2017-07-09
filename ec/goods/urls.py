from django.conf.urls import url
from . import views


urlpatterns = [

    url(r'^$', views.index),
    url(r'^list(\d+)_(\d+)([a-zA-Z_]*)/$', views.list_goods),
    url(r'^detail_(\d+)_(\d+)/$', views.goods_detail),
]