from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.index),
    url(r'^fruit/page/(\d*)', views.fruit),
    url(r'^sort-price-fruit/page/(\d*)', views.sort_price_fruit),
    url(r'^fruit-detail/(\d+)', views.fruit_detail),
]