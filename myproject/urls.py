from django.conf.urls import patterns, include, url
from django.contrib import admin
from cms import views

urlpatterns = [

    url(r'^(\d+)$', views.mostrar_id, name = 'Acceso a page por id'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^(.*)', views.mostrar_name, name = 'Acceso a page por name'),
]
