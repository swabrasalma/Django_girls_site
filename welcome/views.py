from django.shortcuts import render
from django.template import RequestContext
from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect, HttpResponse
from welcome.forms import UserForm, UserProfileForm
from django.contrib.auth import logout

def index(request):
	return render(request,"welcome/index.html",{})

def details(request):
	return render(request,"welcome/details.html",{})


def account(request):
	context = RequestContext(request)
	registered = False
	user_form = UserForm(data=request.POST)
	profile_form = UserProfileForm(data=request.POST)
	if request.method =='POST':
		if user_form.is_valid() and profile_form.is_valid():
			user=user_form.save()
			user.set_password(user.password)
			user.save()
			profile = profile_form.save(commit=False)
			profile_form.user = user

		# if 'picture' in request.FILES:
		# 	profile.picture = request.FILES['picture']
		# 	profile.save()
		# 	registered=True
		# else:
		# 	print("user_form.errors, profile_form.errors")
	else:
		user_form = UserForm()
		profile_form= UserProfileForm()

	return render(request,"welcome/account.html",{'user_form': user_form, 'profile_form':profile_form})

def user_login(request):
	context = RequestContext(request)
	if request.method == 'POST':
		username = request.POST['username']
		password = request.POST['password']
		user = authenticate(username=username, password=password)
		if user is not None:
			if user.is_active:
				login(request, user)
				return HttpResponseRedirect('/welcome/')
			else:
				return HttpResponse("Your django account is disabled successfully.")
		else:
			# print "Invalid login details: {0}, {1}" . format(username, password)
			return HttpResponse("Invalid login cridencials have been supplied. Please retry")
	else:
		return render('welcome/login.html', {})

# @login_required
def user_logout(request):
	logout(request)
	return HttpResponseRedirect('/rango/')
