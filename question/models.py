#question models belong here

from django.db import models
from django import forms
from django.forms import ModelForm

class Question(models.Model):
	title		= models.CharField('Title', max_length=300)
	subject 	= models.CharField('Subject', max_length=300)
	content 	= models.CharField('Question', max_length=300)
	ask_date 	= models.DateField(auto_now_add = True)
	
	def __str__(self):
		return '%s' % (self.title)
		
class QuestionForm(ModelForm):
	class Meta:
		model	= Question