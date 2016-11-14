from welcome.models import UserProfile
from django.contrib.auth.models import User
from django import forms
from .models import Post
from .models import Event
from django.forms import ModelForm
from .models import commentData

class UserForm(forms.ModelForm):
	password1 = forms.CharField(label='password', widget=forms.PasswordInput())
	password2 = forms.CharField(label='password(Again)', widget=forms.PasswordInput())

	def clean_password2(self):
		if 'password1' in self.cleaned_data:
			password1 = self.cleaned_data['password1']
			password2 = self.cleaned_data['password2']
			if password1 == password2:
				return password2
		raise forms.ValidationError('Passwords dont match')

	class Meta:
		model = User
		fields = ('username','first_name','last_name', 'email')
       
class UserProfileForm(forms.ModelForm):
	class Meta:
		model = UserProfile
		fields = ['city']

class AddPost(forms.ModelForm):
	class Meta:
		model = Post
		fields = ('author','title','text','created_date','published_date')

class Addevent(forms.ModelForm):
	class Meta:
		model = Event
		fields = ('date','details','time')

class LoginForm(forms.Form):
	username=forms.CharField(required=True)
	password=forms.CharField(required=True, widget=forms.PasswordInput)

	
class CommentForm(ModelForm):
	class Meta:
		model = commentData
		fields = ["username", "comment",
				]
# def save(self, commit=True):
# 	user = super(UserForm, UserProfileForm)
# 	user.username = self.cleaned_data["username"]
# 	user.email = self.cleaned_data["email"]
# 	user.first_name = self.cleaned_data["first_name"]
# 	user.last_name = self.cleaned_data["last_name"]
# 	user.password = self.cleaned_data["password"]
# 	if commit:
# 		user.save()
# 	return user