from django.urls import path
from .import views


app_name = 'User'

urlpatterns = [
    path('login', views.LoginView),
    path('localsearchsystem', views.UserView, name='localsearchsystem'),
    path('login', views.LogoutView, name = "logout"),
    path('usermanagement', views.UserManagementView, name = "usermanagement"),

]