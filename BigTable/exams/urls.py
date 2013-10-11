from django.conf.urls import patterns, include, url
from exams import views

urlpatterns = patterns('',
    url(r'^$',views.index, name= 'index'),
    url(r'^patients/$', views.patient_list, name='patient_list'),
    url(r'^patients/search', views.patient_list, name='patient_list'),    
    url(r'^(?P<patient_id>\d+)/$',views.detail,name='detail'),
    url(r'^new$',views.add_patient,name='new'),
    url(r'^(?P<patient_id>\d+)/(?P<examination_id>\d+$)',views.new_examination,name='add_detail'),
    url(r'^(?P<patient_id>\d+)/new_examination',views.new_examination,name='new_exam'),
    url(r'^(?P<patient_id>\d+)/new_remind',views.new_examination,name='new_note'),
    url(r'^(?P<patient_id>\d+)/(?P<examination_id>\d+)/modify_examination',views.modify_examination,name='detail2'),
    url(r'^(?P<patient_id>\d+)/modify_reminder',views.modify_reminder,name='detail2'),
    url(r'^(?P<patient_id>\d+)/delete',views.delete_patient,name='deletion'),
    url(r'^(?P<patient_id>\d+|new)/upload/',include('multiuploader.urls')),
    url(r'^(?P<patient_id>\d+)/(?P<examination_id>\d+)/perfetc/',include('perfetc.urls'),name='add_detail'),

)