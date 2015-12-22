from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    url(r'^transactions/', include('transactions.urls',namespace='transactions')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^upload/', include('uploader.urls')),
)
