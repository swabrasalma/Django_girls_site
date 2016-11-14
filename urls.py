from django.conf.urls import patterns, url
from welcome import views
from django.conf import settings
from django.conf.urls.static import static
from welcome import views as welcome_views

urlpatterns = patterns('',
	url(r'^$', views.index, name='index'),
	
	url(r'^details/$', views.details, name='details'),

	url(r'^account/$', views.account, name='account'),

	url(r'^projects/$', views.projects, name='projects'),

	url(r'^blog/$', views.addpost, name='blog'),

	url(r'^post_list/$', views.post_list, name='post_list'),

	url(r'^gallery/$', views.gallery, name='gallery'),

	url(r'^reviewposts/$', views.reviewpost, name='reviewposts'),

	url(r'(?P<post_id>[0-9]+)/approve/$', views.approvePosts, name='approve'),

	url(r'^calender/$', views.event_list, name='calender'),

	url(r'^login/$', views.login_user, name='login'),

	url(r'^logout/$', views.logout, name='logout'),
	
)