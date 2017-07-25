from django.conf.urls import patterns, include, url

from django.contrib import admin
from django.conf import settings
from hello import views as views42cc
admin.autodiscover()

urlpatterns = []

if settings.DEBUG is True:
    # So that it does not conflict with home directory.
    urlpatterns += patterns(
        '',
        (
            r'^uploads/(?P<path>.*)$',
            'django.views.static.serve',
            {'document_root': settings.MEDIA_ROOT}
        )
    )

urlpatterns += patterns(
    '',
    # Examples:
    # url(r'^$', 'fortytwo_test_task.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^requests/', views42cc.latest_requests, name="requests"),
    url(r'^edit_info/', views42cc.edit_info, name="edit_personal_data"),
    url(
        r'^accounts/login/$',
        'django.contrib.auth.views.login',
        {'template_name': 'hello/login.html'},
        name="login"
    ),
    url(r'^', views42cc.homepage_visitor, name="visitor_homepage"),

)
