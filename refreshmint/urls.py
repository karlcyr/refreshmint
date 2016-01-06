from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = patterns('',
    url(r'^transactions/', include('transactions.urls',namespace='transactions')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^upload/', include('uploader.urls', namespace='uploader')),
) + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
