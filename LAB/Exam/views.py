from django.shortcuts import render
from Questions.models import Question
from django.contrib.auth.decorators import login_required


@login_required(login_url='/login_user/')
def exam_view(request, id, points=0):
	question = Question.objects.get(pk=id)
	return render(request, 'exam.html', {'question': question, 'points': points})


@login_required(login_url='/login_user/')
def results(request, points):
	context = {
		'passed': '',
		'points': points
	}
	if points >= 50:
		context['passed'] = 'Yes'

	return render(request, 'results.html', context)


@login_required(login_url='/login_user/')
def answer(request, id):
	correct = request.POST.get('q')
	points = int(request.POST.get('points'))
	if correct == 'correct':	
		if id >= len(Question.objects.all()):
			return results(request, points+25)
		else:
			return exam_view(request, id+1, points+25)

	else:
		if id >= len(Question.objects.all()):
			return results(request, points)
		else:
			return exam_view(request, id+1, points)