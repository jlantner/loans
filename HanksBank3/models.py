from django.db import models

from django.utils import timezone
import datetime



class Question(models.Model):

	question_text = models.CharField(max_length=200)
	pub_date = models.DateTimeField('date published')
#class X(models.Model):
#	text=("Ok. Come back when you want a loan")

	

	def was_published_recently(self):
		now = timezone.now()

		return now - datetime.timedelta(days=1) <= self.pub_date <= now
		was_published_recently.admin_order_field='pub_date'
		was_published_recently.boolean=True
		was_published_recently.short_description='Published recently?'
	def date(self):
		return timezone.now()
	#def was_published_recently_yes_or_no(x):
	#	x=was_published_recently(self)
	#	if x==False:
	#		return "No"
	#	else:
	#		return "Yes"
	def past_or_now(self):
		now=timezone.now()
		return now >= self.pub_date

	
		
	def __str__(self):
		return self.question_text

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    def __str__(self):
    	return self.choice_text
# Create your models here.


# Create your models here.
