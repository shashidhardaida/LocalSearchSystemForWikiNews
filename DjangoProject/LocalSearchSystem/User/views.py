from django.http import HttpResponseRedirect
from django.shortcuts import render
from .models import User
from .import views
from .forms import LoginForm

# Create your views here.

def LoginView(request):
    return render(request, 'index.html')


def UserManagementView(request):
    data = User.objects.all()
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        print(username)
        print(password)
    return render(request, 'user-management.html',{'data':data})


def LogoutView(request):
    return render(request, 'index.html')

