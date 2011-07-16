from django.http import HttpResponse
from django.shortcuts import render_to_response

#from django.contrib.auth import login
#from django.contrib.auth.forms import AuthenticationForm
#from django.shortcuts import render
#from django.shortcuts import HttpResponseRedirect
#from django.core.urlresolvers import reverse

def homepage(request):
	if request.user.is_authenticated():
		return HttpResponse("Home page")

	return render_to_response("login.html")

	#auth_form = AuthenticationForm(None, request.POST or None)
	#nextpage = request.GET.get('next', reverse('index'))
	#if auth_form.is_valid():
	#	login(request, auth_form.get_user())
	#	return HttpResponseRedirect(nextpage)
	#return render(request, 'login.html', {
	#	'auth_form': auth_form,
	#	'title': 'User Login',
	#	'next': nextpage,
	#})
