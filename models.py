from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class UserProfile(models.Model):
	user = models.OneToOneField(User)
	city = models.CharField(max_length=15,null=True)

	def __unicode__(self):
		return self.user.username

class Post(models.Model):
	author = models.ForeignKey('auth.User')
	title = models.CharField(max_length=200)
	text = models.TextField()
	created_date = models.DateTimeField(
	default=timezone.now)
	published_date = models.DateTimeField(
	blank=True, null=True)
	is_published = models.BooleanField(default=False)

	def publish(self):
		self.published_date = timezone.now()
		self.save()
		
	def __str__(self):
		return self.title

class Event(models.Model):
	date = models.DateTimeField(blank=True, null=True)
	details = models.CharField(max_length=200)
	time = models.CharField(max_length=40)

	def __str__(self):
		return self.details

# class Image(models.Model):
	# image= models.ImageField()

class Comment(models.Model):
	post=models.ForeignKey('welcome.Post')

class commentData(models.Model):
	# event=models.ForeignKey('welcome.Event')
	comment=models.TextField(max_length=1000)
	username=models.CharField(max_length=200)