from django.conf.urls import patterns, include, url
from django.views.generic import RedirectView

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns(
    '',
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/', include(admin.site.urls)),

    url(r'^admin/password_reset/$', 'django.contrib.auth.views.password_reset', name='password_reset'),
       (r'^password_reset/done/$', 'django.contrib.auth.views.password_reset_done'),
    url(r'^reset/(?P<uidb36>[0-9A-Za-z]+)-(?P<token>.+)/$', 'django.contrib.auth.views.password_reset_confirm'),
       (r'^reset/done/$', 'django.contrib.auth.views.password_reset_complete'),

    url(r'^search/', include('haystack.urls')),

    url('', include('paste.urls')),
    url('', include('social.apps.django_app.urls', namespace='social')),
)
