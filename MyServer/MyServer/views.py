from django.http import HttpResponse
from MyServer import models
from django.shortcuts import render
import logging



logging.basicConfig(filename='/opt/arpith/logger/logfile', level=logging.DEBUG)


def Registration(request):

	email = request.GET.get('email')
	phoneno = request.GET.get('phoneno')
	
	logger(email)
	logger(phoneno)
	registration = models.Registration()
	registration.email = email
	registration.phoneno = phoneno
	registration.save()

	for e in models.Registration.objects.filter(email=email):
		print e.email, e.phoneno
		
	return HttpResponse([phoneno,email])



def GetFilterCount(request):
	logger ("in getCount")
	logger("Total no of records by the emailId "+request.GET.get('email')+" is " +str(models.Registration.objects.filter(email=request.GET.get('email')).count()))
	return HttpResponse("Total no of records by the emailId "+request.GET.get('email')+" is " +str(models.Registration.objects.filter(email=request.GET.get('email')).count()))


def GetFilterList(request):
	logger( "in GetList")
	return HttpResponse(models.Registration.objects.filter(email=request.GET.get('email')))

def GetAllList(request):
	logger( "In GetAllList")
	return HttpResponse(models.Registration.objects.all())

def logger(comment):
	print "in logger"
	logging.debug("from logger "+comment)

