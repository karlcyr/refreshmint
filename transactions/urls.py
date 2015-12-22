from django.conf.urls import url

from . import views

app_name = 'transactions'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^(?P<transaction_id>[0-9]+)/$', views.view, name='view'),
    url(r'^(?P<transaction_id>[0-9]+)/edit/$', views.edit, name='edit'),
    url(r'^gettrans/',views.gettrans, name='gettrans'),
]


