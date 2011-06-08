from django.http import HttpResponse
from django.shortcuts import render_to_response
import datetime

def homepage(request):
	if request.user.is_authenticated():
		return HttpResponse("Home page")
	else:
		return render_to_response('login.html')

def hello(request):
	return HttpResponse("Hello world")
