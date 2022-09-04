from django.shortcuts import render
from .models import Lesson
from django.db.models import Q
from django.views.generic import ListView
from django.contrib.auth.decorators import login_required


@login_required
def lesson(request, id):
	lesson = Lesson.objects.get(pk=id)
	return render(request, 'lesson.html', {'lesson': lesson})


@login_required
def simulation(request, id):
	lesson = Lesson.objects.get(pk=id)
	return render(request, 'simulation.html', {'simulation': lesson.simulation, 'lesson_id': id})


@login_required
def question(request, id):
	lesson = Lesson.objects.get(pk=id)
	return render(request, 'question.html', {'question': lesson.question, 'lesson_id': id})


@login_required
def success(request):
	return render(request, 'success.html', {})


class lessons_view(ListView):
	model = Lesson
	template_name = 'lessons.html'
	
	def get_queryset(self):
		object_list = Lesson.objects.all()
		return object_list


class lessons_view_search(ListView):
	model = Lesson
	template_name = "lessons.html"

	def get_queryset(self):
		query = self.request.GET.get("search")
		object_list = Lesson.objects.filter(Q(name__icontains=query))
		return object_list