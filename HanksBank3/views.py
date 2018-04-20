from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views import generic
from django.utils import timezone
import datetime 
from django.http import HttpResponse

from .models import Choice, Question
def form(request):
	#try:
	#	question = get_object_or_404(Question, pk=question_id)
	#except Question.DoesNotExist:
	#	raise Http404("Question does not exist")
	return render(request, 'HanksBank3/getLoan.html')

def menu(request):
	return render(request, 'HanksBank3/menu.html')

def no(request):
	return render(request, 'HanksBank3/no.html')

def decision(request):

	try:
		firstname = request.GET["firstname"]
		lastname = request.GET["lastname"]
		age = request.GET["age"]
		highschool = request.GET["highschool"]
		college1 = request.GET["college1"]
		college2 = request.GET["college2"]
		college3 = request.GET["college3"]
		major = request.GET["major"]
		salery = request.GET["salery"]
		
		
		if int(age)<18:
			info=("You must be 18 or older to recieve a loan")
		elif college1=="MIT" or college2=="MIT" or college3=="MIT":
			info=("Loan Accepted")
		elif major == "philosophy" and int(salery)>1000000000 or major == "Philosophy" and int(salery)>1000000000:
			info=("I don't thing your going to make " + salery + " dollers with a philosophy major")
	
		elif major!="Engineering" and int(salery)>2000000000 and major!= "engineering" :

			info = ("Are you kidding? You can't make that much immediately after college as an " + major + " major -loan denied") 
		
		else:
			info = ("Loan Accepted")
	
		for x in range(len(firstname)):
			if str(firstname[x]).isdigit():
				info = ("First and last name must only consist of letters")
				break

		for y in range(len(lastname)):
			if str(lastname[y]).isdigit():
				info = ("First and last name must only consist of letters")
				break

		return HttpResponse(info)



# Create your views here.



	except:
		info=("")
		return HttpResponse(info)


	 #{'question': question})

#def decision(request):y
#	return render(request, 'HanksBank3/decision.html')
class student:
	def __init__(self, firstname, lastname, age, highschool, college1, college2, college3, major, salery):
		self.firstname=firstname
		self.lastname=lastname
		self.age=age
		self.highschool=highschool
		self.college1=college1
		self.college2=college2
		self.college3=college3
		self.major=major
		self.salery=salery

	def info(self):
		return (self.firstname + self.lastname + self.age + self.highschool + self.college1 + self.college2 + self.college3 + self.major + self.salary)
#student_1=student("Jared", "Lantner", "18", "Summit", "Harvord", "Stanford", "Yale", "Physics", "200000000000")
#student_1.info()
#	student_1=student("Jared", "Lantner", "18", "Summit", "Harvord", "Stanford", "Yale", "Physics", "200000000000")
#	student_1.info(def testing(self):
#)
#	return HttpResponse(student.info(student_1))

	def process(self):




		
		
		if int(self.age)<20:
			info=("You must be 18 or older to recieve a loan")
		elif self.college1=="MIT" or self.college2=="MIT" or self.college3=="MIT":			
			info=("Loan Accepted")
		elif self.major == "philosophy" and int(self.salery)>1000000000 or self.major == "Philosophy" and int(self.salery)>1000000000:
			info=("I don't thing your going to make " + self.salery + " dollers with a philosophy major")	
		elif self.major!="Engineering" and int(self.salery)>50000:

			info = ("Are you kidding? You can't make that much immediately after college as an" + self.major + " major -loan denied") 
		
		else:
			info = ("Loan Accepted")
	
		for x in range(len(self.firstname)):
			if str(self.firstname[x]).isdigit():
				info = ("First and last name must only consist of letters")
				break

		for y in range(len(self.lastname)):
			if str(self.lastname[y]).isdigit():
				info = ("First and last name must only consist of letters")
				break

		return HttpResponse(info)



# Create your views here.






def results(request):
	

	try:

		firstname = request.GET["firstname"]
		lastname = request.GET["lastname"]
		age = request.GET["age"]
		highschool = request.GET["highschool"]
		college1 = request.GET["college1"]
		college2 = request.GET["college2"]
		college3 = request.GET["college3"]
		major = request.GET["major"]
		salery = request.GET["salery"]
		student_x=student(firstname,lastname, age, highschool, college1, college2, college3, major, salery)
		student_x.process()
		return HttpResponse(student.process(student_x))

	except:
		return HttpResponse("")




	

		
	#for x in range(len(fname)):
	#	if str(fname[x]).isdigit():
	#		print ("Your name cannot contain any numbers")
	#		fname = ("Error! Name is invalid!")
	#		break
	

	#for x in str(firstname):
		#if str(x).isdigit:
		#	info = ("Name must only consist of letters")
		#	break

	#for y in str(lastname):
		#if str(x).isdigit:
		#	info = ("Name must only consist of letters")
		#	break








# Create your views here.
