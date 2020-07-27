from django.http import HttpResponseRedirect
from django.shortcuts import render
from .models import User
from .import views
from .forms import NewUserForm
from django.contrib.auth import authenticate, login, logout
from django.template.context_processors import csrf
from django.utils.datastructures import MultiValueDictKeyError




# Create your views here.

def LoginView(request):
    return render(request, 'index.html')


# def UserView(request):
#     data = User.objects.all()
#     if request.method == "POST":
#         username = request.POST.get("username")
#         password = request.POST.get("password")
#         print(username)
#         print(password)
#         if username == 'admin':
#             return render(request, 'user-management.html',{'data':data})
#         elif username == 'anonymous':
#             return SearchView(request)


def SearchView(request):
    return render(request, 'search.html')

def LogoutView(request):
    return render(request, 'index.html')

def UserManagementView(request):
    form = NewUserForm(request.POST)
    if request.method == 'POST':
        try:
            print(form.data)
            model = User()
            model.email = form.data['email']
            model.password = form.data['password']
            try:
                admin = request.POST['isadmin']
            except MultiValueDictKeyError:
                admin = False
            if 'isadmin' in form.data:
                model.admin = True
            else:
                model.admin = False
            model.staff = True
            model.active = True
            model.save()
            # return render(request, 'user-management.html')
        except:
            data = User.objects.all()
            return render(request, 'user-management.html', {'data': data})
    data = User.objects.all()
    return render(request, 'user-management.html', {'data': data})


