#answer views here

from django.contrib.auth.decorators import login_required
from django.core.context_processors import csrf
from django.shortcuts import render, get_object_or_404
from answer.models import Answer, AnswerForm
from question.models import Question

@login_required
def display_answers(request, q_id):
	question = get_object_or_404(Question, id=q_id)
	ans_list = Answer.objects.filter(Answer__question=q_id)
	context = {'question': question, 'ans_list': ans_list}
	return render(request, 'view_answers.html', context)
	
def answer_question(request, q_id):
	if request.POST():
		ansform = AnswerForm(request.POST)
		if ansform.is_valid():
			q = get_object_or_404(Question, id=q_id)
			new_answer = Answer(question = q_id, content=ansform.cleaned_data['content'])
			new_answer.save()
			return render(request, 'success.html')
		else:
			context = {'ansform': ansform}
			return render(request, 'ask_question.html', context)
	else:
		ansform = AnswerForm()
		context = {'ansForm': ansform}
		return render(request, 'answer_question.html', context)