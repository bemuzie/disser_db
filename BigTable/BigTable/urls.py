from django.conf.urls import patterns, include, url
import settings

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'BigTable.views.home', name='home'),
    # url(r'^BigTable/', include('BigTable.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    url(r'^reports/', include('exams.urls')),
    url(r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}),
    
    

    

)

urlpatterns += staticfiles_urlpatterns()