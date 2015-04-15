from django.conf.urls import patterns, include, url
from django.conf.urls.static import static
from django.conf import settings
from registration.views import *
from content.views import *

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'NoteZones.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),

    url(r'^$', 'home.views.home'),
    url(r'^guide/', 'home.views.guide'),
    url(r'^submit/', submit),
    url(r'^login/', login),
    url(r'^logout/', 'content.views.logout'),
    url(r'^forgot_password/', forgot_password),
    url(r'^successful_password/', successful_password),
    url(r'^successful/', successful),
    url(r'^successful_login/', successful_login),
    url(r'^content/', 'content.views.content'),
    url(r'^home/', 'content.views.content_home'),
    url(r'^content_guide/', 'content.views.content_guide'),
    url(r'^(?P<pk>\d+)/delete/$', 'content.views.detail_delete', name='detail_delete'),
) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
