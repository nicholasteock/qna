#question views here
from django.contrib.auth.decorators import login_required
from django.core.context_processors import csrf
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from question.models import Question, QuestionForm

@login_required
def	display_questions(request):
	list = Question.objects.all()
	context = {'title': 'Display Questions', 'list': list}
	return render(request, 'display_questions.html', context)

@login_required
def ask_question(request):
	if request.POST:
		askform = QuestionForm(request.POST)
		if askform.is_valid():
			new_question = Question(title = askform.cleaned_data['title'], subject = askform.cleaned_data['subject'], content = askform.cleaned_data['content'])
			new_question.save()
			return render(request, 'success.html')
		else:
			context = {'askform': askform}
			return render(request, 'ask_question.html', context)
	else:
		askform = QuestionForm()
		context = {'askform': askform}
		return render(request, 'ask_question.html', context)