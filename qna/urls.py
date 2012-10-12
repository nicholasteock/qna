from django.conf.urls import patterns, include, url
from django.contrib import admin
from question.views import ask_question, display_questions
from answer.views import display_answers, answer_question
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
	url(r'^questions/$', 'question.views.display_questions'),
	url(r'^ask/$', 'question.views.ask_question'),
	url(r'^display_answers/(?P<q_id>\d+)\d+/$', 'answer.views.display_answers'),
	url(r'^answer/(?P<q_id>\d+)/$', 'answer.views.answer_question', 'answer_question'),
)
