from django.shortcuts import render
from models import Item

def list(request):
	results = Item.objects.filter(user=request.user)
	return render(request, 'list.html', {'results':results})
