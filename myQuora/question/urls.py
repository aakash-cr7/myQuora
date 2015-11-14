from django.conf.urls import url
urlpatterns = [
    url(r'^create/$', 'question.views.create_question', name='create_question'),
    url(r'^myquestions/$', 'question.views.myquestions', name='myquestions'),
    url(r'^myquestions/(?P<page_num>\d+)/$', 'question.views.myquestions', name='myquestions_with_page'),
    url(r'^search/$', 'question.views.search', name='searchquestions'),
    url(r'^(?P<question_id>\d+)/$', 'question.views.question_info', name='question_info'),
    url(r'^upvote/(?P<ans_id>\d+)/$', 'question.views.upvote_ans', name='upvote_ans'),
]

