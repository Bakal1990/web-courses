from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    url(r'^polls/', include('polls.urls', 'polls')),
    url(r'^admin/', include(admin.site.urls)),
)
