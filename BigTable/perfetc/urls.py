from django.conf.urls import patterns, include, url
from perfetc import views

urlpatterns = patterns('',
    url(r'^$',views.circulation, name= 'graph'),
    )