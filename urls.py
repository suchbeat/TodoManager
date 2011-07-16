from django.conf.urls.defaults import patterns, include, url
<<<<<<< HEAD
from TodoManager.views import homepage
from TodoManager.registration import views
=======
from TodoManager import views
>>>>>>> 1bf3fb0c6e6a93e912c447ab7e6b8a6ed7ab0265

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
<<<<<<< HEAD
	url(r'^$', homepage),
	url(r'^register/$', views.register),
=======
	url(r'^$', views.homepage),
	url(r'^hello/$', views.hello),
>>>>>>> 1bf3fb0c6e6a93e912c447ab7e6b8a6ed7ab0265
    # Examples:
    # url(r'^$', 'TodoManager.views.home', name='home'),
    # url(r'^TodoManager/', include('TodoManager.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)

urlpatterns += patterns('TodoManager.registration.views',
	url(r'^login/$', 'login'),
	url(r'^logout/$', 'logout'),
)
