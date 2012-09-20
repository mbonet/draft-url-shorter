from django.conf.urls import patterns, url

from wrapp import views

urlpatterns = patterns('',
    url(r'^$', views.homepage),
    url(r'^wrapp/(?P<key>.{6})/$', views.resolve),
)

