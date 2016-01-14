from django.conf.urls import url, patterns, include
from django.conf.urls.static import static
from django.conf import settings

from . import views
from .views import UploadFileView, DataFileDetailView, DataFileIndexView

app_name = 'uploader'
urlpatterns = patterns('',
    url(r'^$', DataFileIndexView.as_view(), name='home'),
    url(r'^add/', UploadFileView.as_view(), name='data_file_upload'),
    url(r'^uploaded/(?P<pk>\d+)/$', DataFileDetailView.as_view(), name='datafile'),
    url(r'^edit_data/$', views.edit_data, name='edit_data'),

) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


