from django.conf.urls import url
urlpatterns = [
    url(r'^(?P<question_id>[0-9]+)/$', 'question.views.question_info', name = 'question_info'),
]

