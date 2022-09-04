from django.urls import path
from .views import lessons_view, lessons_view_search, lesson, simulation, question, success

urlpatterns = [
	path('', lessons_view.as_view(), name="Lessons"),
	path('search_results/', lessons_view_search.as_view(), name="Lessons search"),
	path('<int:id>', lesson, name="Lesson"),
	path('simulation/<int:id>', simulation, name="Simulation"),
	path('question/<int:id>', question, name="Question"),
	path('success', success, name="Success"),
]