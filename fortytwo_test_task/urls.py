from django.conf.urls import patterns, include, url

from django.contrib import admin
from hello import views as assignment_views
admin.autodiscover()

urlpatterns = patterns(
    '',
    # Examples:
    # url(r'^$', 'fortytwo_test_task.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^', assignment_views.homepage_visitor, name="visitor_homepage"),

)
