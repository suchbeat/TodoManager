from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render
from django.shortcuts import HttpResponseRedirect
from django.contrib.auth.forms import UserCreationForm

def register(request):
	if request.user.is_authenticated():
		return HttpResponseRedirect('/list/')

	if request.method == 'POST':
		form = UserCreationForm({'username':request.POST['username'], 'password1':request.POST['password'], 'password2':request.POST['password']})
		if form.is_valid():
			new_user = form.save()
			login(request, authenticate(username=request.POST['username'], password=request.POST['password']))
			return HttpResponseRedirect('/list/')
		else:
			return render(request, 'login.html', {'error':'Incorrect data entered!'})
	else:
		return render(request, 'login.html')

def login_view(request):
	if request.user.is_authenticated():
		return HttpResponseRedirect('/list/')

	if request.method == 'POST':
		user = authenticate(username=request.POST['username'], password=request.POST['password'])
		if user is not None:
			if user.is_active:
				login(request, user)
				return HttpResponseRedirect('/list/')
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
