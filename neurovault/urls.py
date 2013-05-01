from django.conf.urls import patterns, include, url
from django.conf import settings
from django.contrib import admin
from .views import view_profile, edit_user
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^studies/', include('statmaps.urls', namespace="statmaps")),
    url(r'^admin/', include(admin.site.urls)),
    url(r'', include('social_auth.urls')),
    url(r'^accounts/login/$', 'django.contrib.auth.views.login', 
        {'template_name': 'registration/login.html'}, name="login"),
    url(r'^accounts/logout/$', 'django.contrib.auth.views.logout', 
        {'template_name': 'registration/logout.html'}, name="logout"),
    url(r'^accounts/create/$',
        edit_user,
        name="create_user"),
    url(r'^accounts/profile/.*$',
        view_profile,
        name="my_profile"
        ),    
    url(r'^accounts/(?P<username>[A-Za-z@/./+/-/_]+)/edit$',
        edit_user,
        name="edit_user"
        ),
    url(r'^accounts/(?P<username>[A-Za-z@/./+/-/_]+)/$',
        view_profile,
        name="profile"
        ),
                  
)

if settings.DEBUG:
    # static files (images, css, javascript, etc.)
    urlpatterns += patterns('',
        (r'^media/(?P<path>.*)$', 'django.views.static.serve', {
        'document_root': settings.MEDIA_ROOT}))