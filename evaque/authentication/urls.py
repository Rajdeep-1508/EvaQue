from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path('',views.homePage,name="home"),
    path('about',views.about,name="about"),
    path('login',views.signin,name="login"),
    path('signup',views.signup,name="signup"),
    path("logout",views.signout,name="logout"),
    path("beginner-form",views.begForm,name="begform")
]
