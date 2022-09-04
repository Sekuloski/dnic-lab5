from django.db import models

# Create your models here.
class Lesson(models.Model):
	name = models.CharField(max_length=100)
	text = models.TextField()
	video = models.TextField(null=True, blank=True)
	simulation = models.CharField(max_length=100)
	question = models.ForeignKey('Questions.Question', on_delete=models.SET_NULL, null=True, blank=True)

	def __str__(self):
		return self.name