from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    
    # url(r'^$', 'MyServer.views.home', name='home'),
    url(r'^Registration', 'MyServer.views.Registration', name='Registration'),
    url(r'^GetFilterCount', 'MyServer.views.GetFilterCount', name='GetFilterCount'),
    url(r'^GetFilterList', 'MyServer.views.GetFilterList', name='GetFilterList'),
    url(r'^GetAllList', 'MyServer.views.GetAllList', name='GetAllList'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
)
