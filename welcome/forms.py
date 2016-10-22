from welcome.models import UserProfile
from django.contrib.auth.models import User
from django import forms

class UserForm(forms.ModelForm):
	password = forms.CharField(widget=forms.PasswordInput())
	
	class Meta:
		model = User
		fields = ('username', 'email', 'password')

class UserProfileForm(forms.ModelForm):
	class Meta:
		model = UserProfile
		fields = ('website',)

def save(self, commit=True):
	user = super(UserForm, UserProfileForm)
	user.username = self.cleaned_data["username"]
	user.email = self.cleaned_data["email"]
	user.password = self.cleaned_data["password"]
	if commit:
		user.save()
	return user