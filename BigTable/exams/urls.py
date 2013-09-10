from django.conf.urls import patterns, include, url
from exams import views


urlpatterns = patterns('',
    url(r'^$',views.index, name= 'index'),
    url(r'^patients/$', views.patient_list, name='patient_list'),
    url(r'^(?P<patient_id>\d+)/',views.detail,name='detail'),
    url(r'^new',views.add_patient,name='new'),
)