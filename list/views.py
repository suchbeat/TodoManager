from django.shortcuts import render
from django.shortcuts import HttpResponseRedirect
from models import Item

def list(request):
	if not request.user.is_authenticated():
		return HttpResponseRedirect('/')
	results = Item.objects.filter(user=request.user)
	return render(request, 'list.html', {'results':results})
