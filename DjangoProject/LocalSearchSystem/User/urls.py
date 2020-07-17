from django.urls import path
from .import views

app_name = 'User'

urlpatterns = [
    path('login', views.LoginView),
    path('usermanagement', views.UserManagementView, name='usermanagement'),
    path('login', views.LogoutView, name = "logout"),

]