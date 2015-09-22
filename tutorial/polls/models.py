from django.db import models

class Question(models.Model):
	text = models.CharField(max_length = 200)
	date = models.DateTimeField("date published")
	
	def __str__(self):
		return self.text
		
	def was_published_recently(self):
		return self.date >= timezone.now() - datetime.timedelta(days = 1)
	
class Choice(models.Model):
	question = models.ForeignKey(Question)
	text = models.CharField(max_length = 200)
	votes = models.IntegerField(default = 0)
	
	def __str__(self):
		return self.text