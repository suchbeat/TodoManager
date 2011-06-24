from django.http import HttpResponse
#from django.shortcuts import render_to_response
#import datetime

from django.contrib.auth import login
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render
#from django.shortcuts import HttpResponseRedirect
from django.core.urlresolvers import reverse

def homepage(request):
	if request.user.is_authenticated():
		return HttpResponse("Home page")
		#return HttpResponseRedirect(reverse('index'))

	# Initialize the form either fresh or with the appropriate POST data as the instance
	auth_form = AuthenticationForm(None, request.POST or None)
 
    # Ye Olde next param so common in login.
    # I send them to their default profile view.
	#nextpage = request.GET.get('next', reverse('index'))
 
    # The form itself handles authentication and checking to make sure passowrd and such are supplied.
	if auth_form.is_valid():
		login(request, auth_form.get_user())
		#return HttpResponseRedirect(nextpage)
 
	return render(request, 'login.html', {
		'auth_form': auth_form,
		'title': 'User Login',
		#'next': nextpage,
	})

def hello(request):
	return HttpResponse("Hello world")
