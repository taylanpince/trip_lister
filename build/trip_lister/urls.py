from django.conf.urls.defaults import *


urlpatterns = patterns('',
    # Trip URLs
    (r'^$', include('trips.urls')),
    
    # Login
    url(r'^login/$', 'django.contrib.auth.views.login', name='user_login'),
    
    # Logout
    url(r'^logout/$', 'django.contrib.auth.views.logout', name='user_logout'),
)
