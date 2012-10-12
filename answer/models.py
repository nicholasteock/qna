#answer models here

from django.db import models
from django import forms
from django.forms import ModelForm
from question.models import Question

class Answer(models.Model):
	question	= models.ForeignKey(Question)
	content				= models.CharField('Answer', max_length = 300)
	answer_date			= models.DateField(auto_now_add = True)
	
	def __str__(self):
		return "%s" % (self.content)
	
class AnswerForm(ModelForm):
	class Meta:
		model = Answer
		