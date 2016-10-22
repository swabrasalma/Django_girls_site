from django.conf.urls import patterns, url
from welcome import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = patterns('',
	url(r'^$', views.index, name='index'),
	
	url(r'^details/$', views.details, name='details'),

	url(r'^account/$', views.account, name='account'),

	url(r'^login/$', views.user_login, name='login'),

	url(r'^logout/$', views.user_logout, name='logout'),
	
)