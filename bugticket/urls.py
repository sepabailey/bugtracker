from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='homepage'),
    path('login/', views.loginview, name='login_url'),
    path('logout/', views.logoutview, name='logout_url'),
    path('signup/', views.adduser, name='signup'),
]
