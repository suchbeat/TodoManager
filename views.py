from django.http import HttpResponse
import datetime

def homepage(request):
	return HttpResponse("Home page")

def hello(request):
	return HttpResponse("Hello world")
