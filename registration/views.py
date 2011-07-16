from django.http import HttpResponse

def register(request):
	if 'email' in request.POST and request.POST['email']:
		message = 'Your email is: %r' % request.POST['email']
	else:
		message = 'You submitted an empty form.'
	return HttpResponse(message)
