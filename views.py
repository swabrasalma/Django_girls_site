from django.shortcuts import render,get_object_or_404,redirect
from django.template import RequestContext
from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect, HttpResponse
from welcome.forms import UserForm, UserProfileForm, AddPost, Addevent, LoginForm
from django.contrib.auth import logout
from .forms import *
from welcome.models import Post
from welcome.models import Event

def index(request):
	return render(request,"welcome/index.html",{})

def details(request):
	return render(request,"welcome/details.html",{})

def projects(request):
	return render(request,"welcome/projects.html",{})

# def blog(request):
	# posts=Post.objects.all()
	# return render(request,"welcome/blog.html", {'posts':posts})

def calender(request):
	return render(request,"welcome/calender.html",{})

def gallery(request):
	return render(request,"welcome/gallery.html",{})

def addcomment(request):
	print(request)
	if request.method == 'POST':
		form = CommentForm(request.POST)
		if form.is_valid():
			instance = form.save(commit = False)
			instance.comments = form.cleaned_data()
			instance.save()
			data = {'success':True, 'msg':"Success"}
			return Response(data)
	else:
		data = {'success': False, 'msg':'Error'}
		return Response(data)

def addpost(request):
	if request.method == 'POST':
		user_post= AddPost(data=request.POST)
		if user_post.is_valid:
			post = user_post.save()
			# print("Your blog post has been submitted for review")
			return render(request,"welcome/blog.html",{})
		else:
			print("errors")
	else:
		user_post =AddPost()
		return render(request,"welcome/blog.html",{'user_post':user_post})

def post_list(request):
	posts=Post.objects.all().filter(is_published=True)
	return render(request, "welcome/post_list.html", {'posts':posts})

def addevent(request):
	if request.method == 'POST':
		calender_event = Addevent(data=request.POST)
		if calender_event.is_valid:
			event = calender_event.save()
			return HttpResponseRedirect('/welcome/')
		else:
			print("errors")
	else:
		calender_event = Addevent()
		return render(request,"welcome/calender.html", {'calender_event':calender_event})

def event_list(request):
	events=Event.objects.all()
	return render(request, "welcome/calender.html", {'events':events})

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
			profile_form.user = user
			return HttpResponseRedirect('/welcome/')
	else:
		user_form = UserForm()
		profile_form= UserProfileForm()
		return render(request,"welcome/account.html",{'user_form': user_form, 'profile_form':profile_form})


def login_user(request):
	form=LoginForm()
	# import pdb; pdb.set_trace()
	if request.method=='POST':
		form=LoginForm(request.POST)	
		# print("data")	
		if form.is_valid():
			username=form.cleaned_data['username']
			password=form.cleaned_data['password']
			user=authenticate(username=username, password=password)
			if user:
				if user.is_active:
					login(request, user)
					return redirect('index')
				else:
					return HttpResponse("Your account was disabled")
		# else:
			# print (form.errors)
			else:
				print("Invalid login details:{0}, {1}".format(username, password))
				return HttpResponse("Invalid login details supplied")
				# form=LoginForm()
			# return render(request,'welcome/login.html', {'form':form})
	else:
		return render(request,'welcome/login.html', {'form':form})

		

def logout(request):
	logout(request)
	return HttpResponseRedirect('/welcome/')

def reviewpost(request):
	if request.method=='POST':
		if 'Approve' in request.POST:
			print('Approve')
		else:
			pass
	posts = Post.objects.all().filter(is_published=False)
	return render(request, 'welcome/reviewposts.html',{'posts':posts})

def approvePosts(request, post_id):
	post = get_object_or_404(Post, pk=post_id)
	post.is_published=True
	post.save()
	print('Post ID: ',post_id)
	return HttpResponseRedirect('/welcome/')

