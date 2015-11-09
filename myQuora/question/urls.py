from django.conf.urls import url
urlpatterns = [
    url(r'^create/$', 'question.views.create_question', name='create_question'),
    url(r'^myquestions/$', 'question.views.myquestions', name='myquestions'),
    url(r'^myquestions/(?P<page_num>\d+)/$', 'question.views.myquestions', name='myquestions_with_page'),
]

