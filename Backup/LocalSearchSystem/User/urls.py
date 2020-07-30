from django.urls import path
from .import views


app_name = 'User'

urlpatterns = [
    path('login', views.LoginView),
    path('loginaction', views.LoginAction, name='loginaction'),
    path('login', views.LogoutView, name = "logout"),
    path('usermanagement', views.UserManagementView, name = "usermanagement"),
    path('newuser', views.NewUserView, name = "newuser"),
    path('Searchpage', views.SearchView, name = "searchpage"),
]