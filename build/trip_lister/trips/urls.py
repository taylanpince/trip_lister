from django.conf.urls.defaults import *


urlpatterns = patterns('trips.views',
    # Overview
    url(r'^$', 'overview', name='trips_overview'),
    
    # Create
    url(r'^create/$', 'create', name='trips_create'),
    
    # Delete
    url(r'^delete/$', 'delete', name='trips_delete'),
)
