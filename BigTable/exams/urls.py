# -*- coding: utf-8 -*-
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
    url(r'^(?P<patient_id>\d+)/(?P<examination_id>\d+)/modify_examination',views.modify_examination,name='modify_examination'), #Изменение исследования, добавление временных задержек, описание результатов исследования
    url(r'^(?P<patient_id>\d+)/(?P<examination_id>\d+)/modify_phase',views.modify_phase,name='modify_phase'), # добавление, удаление, изменение временных задержек и зоны сканирования каждой фазы исследования
    url(r'^(?P<patient_id>\d+)/(?P<examination_id>\d+)/actions_examination',views.actions_examination,name='actions_examination'), #Контролирует действие кнопочек в списке исследований на странице пациента
    url(r'^(?P<patient_id>\d+)/modify_reminder',views.modify_reminder,name='detail2'),
    url(r'^(?P<patient_id>\d+)/modify_procedure',views.modify_procedure,name='modify_procedure'),
    url(r'^(?P<patient_id>\d+)/modify_analysis',views.modify_analysis,name='modify_analysis'),
    url(r'^(?P<patient_id>\d+)/delete',views.delete_patient,name='deletion'),
    url(r'^(?P<patient_id>\d+|new)/upload/',include('multiuploader.urls')),
    url(r'^(?P<patient_id>\d+)/(?P<examination_id>\d+)/perfetc/',include('perfetc.urls'),name='add_detail'),

)
