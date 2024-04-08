from .views import Login, signup, songpage, songpage2, songpage3
from django.urls import path
from django import views
from webpage import views
from . import views
#from website import webpage

urlpatterns  = [
    path("",views.display,name="show"),
    path("basic/",views.basic,name='basic'),
    path("Login/",views.Login,name='Login'),
    path("signup/",views.signup,name='signup'),
    path("songpage/",views.songpage,name='songpage'),
    path("songpage2/",views.songpage2,name='songpage2'),
    path("songpage3/",views.songpage3,name='songpage3'),


]