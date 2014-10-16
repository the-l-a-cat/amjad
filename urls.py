from django.conf.urls import patterns, include, url
from django.contrib import admin

from amjad import views

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'amjad.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^api/(.*)/(.*)/(.*)', views.api),
    url(r'^api/(.*)/(.*)', views.api),
    url(r'^api/(.*)', views.api),
    # url(r'^api/(?P<function_name>.*)/(?P<function_args>.*)', views.api),
    url(r'^js/(.*\.js)', views.js),
    url('', views.index),
)
