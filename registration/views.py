from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, HttpResponseRedirect
from django.contrib.auth.forms import UserCreationForm

def requires_login(view):
	def new_view(request, *args, **kwargs):
		if not request.user.is_authenticated():
			return HttpResponseRedirect('/login/')
		return view(request, *args, **kwargs)
	return new_view

def register(request):
	if request.user.is_authenticated():
		return HttpResponseRedirect('/')

	if request.method == 'POST':
		form = UserCreationForm({'username':request.POST['username'], 'password1':request.POST['password'], 'password2':request.POST['password']})
		if form.is_valid():
			new_user = form.save()
			login(request, authenticate(username=request.POST['username'], password=request.POST['password']))
			return HttpResponseRedirect('/')
		else:
			return render(request, 'login.html', {'error':'Incorrect data entered!'})
	else:
		return render(request, 'login.html')

def login_view(request):
	if request.user.is_authenticated():
		return HttpResponseRedirect('/')

	if request.method == 'POST':
		user = authenticate(username=request.POST['username'], password=request.POST['password'])
		if user is not None:
			if user.is_active:
				login(request, user)
				return HttpResponseRedirect('/')
			else:
				return render(request, 'login.html', {'error':'Unactive user!'})
		else:
			return render(request, 'login.html', {'error':'Incorrect data entered!'})
	else:
		return render(request, 'login.html')

def logout_view(request):
	if request.user.is_authenticated():
		logout(request)
	return HttpResponseRedirect('/')
