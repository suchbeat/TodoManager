from django.http import HttpResponse
#from django.shortcuts import render_to_response
#import datetime

from django.contrib.auth import login
from django.shortcuts import render
#from django.shortcuts import HttpResponseRedirect
from django.core.urlresolvers import reverse

def homepage(request):
	if request.user.is_authenticated():
		return HttpResponse("Home page")

	return render(request, 'login.html')

def hello(request):
	return HttpResponse("Hello world")
