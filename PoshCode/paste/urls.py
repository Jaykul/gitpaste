from django.conf.urls import patterns, include, url
from django.views.generic import RedirectView

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('PoshCode.paste.views',
    url(r'^live/$', 'live_paste', name='live_paste'),
    url(r'^(?P<pk>\d+)/$', RedirectView.as_view(url= '/paste/%(pk)s/')),
    url(r'^(?P<pk>\d+)/(?P<private_key>[a-zA-Z0-9]+)?/?$', RedirectView.as_view(url= '/paste/%(pk)s/%(private_key)s/')),
    url(r'^owner/$', RedirectView.as_view(url= '/owner/all/')),
    url(r'^owner/anonymous/', 'user_pastes', name='anon_pastes'),
    url(r'^owner/(?P<owner>.+)/', 'user_pastes', name='user_pastes'),
    url(r'^paste/(?P<pk>\d+)/adopt/(?P<private_key>[a-zA-Z0-9]+)?/?$', 'paste_adopt', name='paste_adopt'),
    url(r'^paste/(?P<pk>\d+)/embed/(?P<private_key>[a-zA-Z0-9]+)?/?$', 'paste_embed', name='paste_embed'),
    url(r'^paste/(?P<pk>\d+)/edit/(?P<private_key>[a-zA-Z0-9]+)?/?$', 'paste_edit', name='paste_edit'),
    url(r'^paste/(?P<pk>\d+)/fork/(?P<private_key>[a-zA-Z0-9]+)?/?$', 'paste_fork', name='paste_fork'),
    url(r'^paste/(?P<pk>\d+)/favorite/(?P<private_key>[a-zA-Z0-9]+)?/?$', 'paste_favorite', name='paste_favorite'),
    url(r'^paste/(?P<pk>\d+)/delete/(?P<private_key>[a-zA-Z0-9]+)?/?$', 'paste_delete', name='paste_delete'),
    url(r'^paste/(?P<pk>\d+)/raw/(?P<private_key>[a-zA-Z0-9]+)?/?$', 'paste_raw', name='paste_raw'),
    url(r'^commit/(?P<pk>.+)/adopt/(?P<private_key>[a-zA-Z0-9]+)?/?$', 'commit_adopt', name='commit_adopt'),
    url(r'^commit/(?P<pk>.+)/download/(?P<private_key>[a-zA-Z0-9]+)?/?$', 'commit_download', name='commit_download'),
    url(r'^paste/(?P<pk>\d+)/(?P<private_key>[a-zA-Z0-9]+)?/?$', 'paste_view', name='paste_view'),
    url(r'^users/$', 'users', name='users'),
    url(r'^favorites/$', 'favorites', name='favorites'),
    url(r'^accounts/login/$', 'login', name='login'),
    url(r'^accounts/logout/$', 'logout', name='logout'),
    url(r'^accounts/register/$', 'register', name='register'),
    url(r'^accounts/preference/$', 'preference', name='preference'),
    url(r'^accounts/profile/$', 'preference', name='preference'),
    url(r'^accounts/timezone/$', 'set_timezone', name='set_timezone'),
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/', include(admin.site.urls)),    
    url(r'^$', 'paste', name='paste'),
)
