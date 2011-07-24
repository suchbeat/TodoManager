from django.conf.urls.defaults import patterns, include, url
from TodoManager import views

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
	url(r'^$', include('TodoManager.list.urls')),
    # Examples:
    # url(r'^$', 'TodoManager.views.home', name='home'),
    # url(r'^TodoManager/', include('TodoManager.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)

urlpatterns += patterns('TodoManager.registration.views',
	url(r'^register/$', 'register'),
	url(r'^login/$', 'login_view'),
	url(r'^logout/$', 'logout_view'),
)
