from django.conf.urls.defaults import patterns, include, url
from TodoManager.views import homepage
from TodoManager.registration import views

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
	url(r'^$', homepage),
	url(r'^register/$', views.register),
    # Examples:
    # url(r'^$', 'TodoManager.views.home', name='home'),
    # url(r'^TodoManager/', include('TodoManager.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)
