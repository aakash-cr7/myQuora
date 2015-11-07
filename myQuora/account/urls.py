from django.conf.urls import include, url
urlpatterns = [
    url(r'^logout/$', 'account.views.logout', name = 'logout'),
]
