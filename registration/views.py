from django.contrib.auth import authenticate
from django.contrib.auth import login
from django.shortcuts import render
# from django.shortcuts import HttpResponseRedirect

def login(request):
	if request.method == 'POST':
		user = authenticate(username=request.POST['username'], password=request.POST['password'])
		if user is not None:
			if user.is_active:
				login(request, user)
				# success
				return render(request, '/')
				# return HttpResponseRedirect('/')
			else:
				# disabled account
				return render(request, 'login.html', {'error':'Unactive user!'})
				# return direct_to_template(request, 'inactive_account.html')
		else:
			# invalid login
			return render(request, 'login.html', {'error':'Incorrect data entered!'})
			# return direct_to_template(request, 'invalid_login.html')

def logout(request):
	logout(request)
	return direct_to_template(request, 'logged_out.html')
