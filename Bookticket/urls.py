from django.urls import path
from . import views

urlpatterns = [
      path('', views.home, name='home'),
      path('booktick/', views.booktick),
      path('booktick/home/', views.home),
      path('login/', views.login),
      path('register/', views.signup),
      path('confirm/myticket/', views.myticket),
      path('myticket/', views.myticket),
      path('myticket/home/', views.home),
      path('train/', views.train),
      path('booktick/train/', views.train),
      path('booktick/train/home/', views.home),
      path('booktick/train/booktick/', views.booktick),
      path('booktick/train/login/', views.login),
      path('booktick/train/register/', views.signup),
      path('booktick/train/myticket/', views.myticket),
      path('signup/', views.signup),
      path('booktick/signup/', views.signup),
      path('booknow/', views.booknow),
      path('booknow/home/', views.home),
      path('login/', views.login),
      path('login/home/', views.home),
      path('login/', views.login, name='login_name'),
      path("logout/", views.logout),
      path("home/", views.home),
      path('confirm/', views.confirm),

]