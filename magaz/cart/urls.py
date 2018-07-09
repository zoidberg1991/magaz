from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^remove/(?P<product_id>\d+)/$', views.remove_cart, name='remove_cart'),
    url(r'^add/(?P<product_id>\d+)/$', views.add_cart, name='add_cart'),
    url(r'^$', views.detail_cart, name='detail_cart'),
]