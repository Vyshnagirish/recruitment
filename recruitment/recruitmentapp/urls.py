from django.urls import path
from . import views

urlpatterns = [
    path('', views.body, name = 'body'),
    path('about', views.about, name = 'about'),
    path('job', views.job, name = 'job'),
    path('login', views.loginpage, name = 'loginpage'),
    path('register', views.register, name = 'register'),
    path('home', views.home, name = 'home'),
    path('logout', views.logoutpage, name = 'logoutpage'),

]
