from django.http import HttpResponse
from django.contrib.auth import login
from django.shortcuts import render, HttpResponseRedirect

def homepage(request):
	if request.user.is_authenticated():
		return HttpResponseRedirect('/list/')
	return render(request, 'login.html')
