from django.urls import path
from .views import exam_view, results, answer

urlpatterns = [
	path('<int:id>/', exam_view, name='Exam'),
	path('results/', results, name='Results'),
	path('<int:id>/answer/', answer, name='Answer')
]