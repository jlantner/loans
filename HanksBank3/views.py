#from django.shortcuts import get_object_or_404, render
#from django.http import HttpResponseRedirect
#from django.urls import reverse
#from django.views import generic
#from django.utils import timezone
#imp
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views import generic
from django.utils import timezone
import datetime 
from django.http import HttpResponse

from .models import Choice, Question

def menu(request):
	return render(request, 'HanksBank3/menu.html')
	
def form(request):
	#try:
	#	question = get_object_or_404(Question, pk=question_id)
	#except Question.DoesNotExist:
	#	raise Http404("Question does not exist")
	return render(request, 'HanksBank3/getLoan.html')




def no(request):
	return render(request, 'HanksBank3/no.html')

	 #{'question': question})

#def decision(request):
#	return render(request, 'HanksBank3/decision.html')
	

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


from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views import generic
from django.utils import timezone
import datetime 
from django.http import HttpResponse
import sys

from .models import Choice, Question


#import datetime 
#from django.http import HttpResponse

#from .models import Choice, Question
 
#def form(request):
	#try:
	#	question = get_object_or_404(Question, pk=question_id)
#Harverd.name_set("Harverd")
#Harverd.top_20_set(True) 
#print ("The name is" %s, Harverd.name_get())
#print ("Top 20 is" %s, Harverd.top_20_get())

#def application(request):
#	x=applicant()
#####x.college1 = request.GET["college1"]
	#x#.college2 = request.GET["college2"]
	#x.college3 = request.GET["college3"]
	#x.major = request.GET["major"]
	#x.salery = request.GET["salery"]


	#if int(x.age)<18:
	#		result=("You must be 18 or older to recieve a loan")
#	elif x.college1=="MIT" or x.college2=="MIT" or x.college3=="MIT":
#		result=("Loan Accepted")
#	elif x.major == "philosophy" and int(x.salery)>1000000000 or x.major == "Philosophy" and int(x.salery)>1000000000:			result=("I don't thing your going to make " + salery + " dollers with a philosophy major")

#	elif x.major!="Engineering" and int(x.salery)>2000000000 and x.major!= "engineering" :

#		result = ("Are you kidding? You can't make that much immediately after college as an " + x.major + " major -loan denied") 
		
#	else:
#		result = ("Loan Accepted")
	
#	for y in range(len(x.firstname)):
#		if str(x.firstname[y]).isdigit():
#			x.result = ("First and last name must only consist of letters")
#			break

#	for z in range(len(x.lastname)):
#		if str(x.lastname[z]).isdigit():
#			x.result = ("First and last name must only consist of letters")
#			break

#



























# Create your views here.
