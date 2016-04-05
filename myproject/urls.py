from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',

    url(r'^(\d+)$', 'cms.views.mostrar_id',),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^(.*)', 'cms.views.mostrar_name',),
)
