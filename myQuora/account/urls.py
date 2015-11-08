from django.conf.urls import include, url
urlpatterns = [
    url(r'^logout/$', 'account.views.logout', name = 'logout'),
    url(r'^activate/(?P<uid>\d+)/(?P<token>[0-9A-Za-z_\-]+)/$', 'account.views.activate', name='activate'),
]
