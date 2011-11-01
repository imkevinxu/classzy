from django.conf.urls.defaults import patterns, include, url
from django.conf import settings

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',

	url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
	url(r'^admin/', include(admin.site.urls)),
	
    #url(r'^$', 'views.home'),
	url(r'^create', 'views.create'),
	url(r'^profile', 'views.profile'),
	url(r'^class', 'views.view_class'),
	url(r'^add', 'views.add'),
	
	url(r'^/?$', 'views.home', name='home'),
	url(r'^accounts/login/$','django.contrib.auth.views.login',
        dict(template_name = 'jqm/login.html'), name='login'),
    url(r'^accounts/logout/$','django.contrib.auth.views.logout',
        dict(template_name = 'jqm/logout.html'), name='logout'),
)
