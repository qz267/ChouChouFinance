from django.conf.urls import patterns, include, url
from django.contrib import admin
from spending import views as sp_views

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'finance.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^spending-list/$', sp_views.list_spending),
    url(r'^spending-new/$', sp_views.new_spending),
    url(r'^spending-add/$', sp_views.add_spending),
)
