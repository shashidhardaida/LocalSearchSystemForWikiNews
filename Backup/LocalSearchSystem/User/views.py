from django.http import HttpResponseRedirect
from django.shortcuts import render
from .models import WikiNewsUser
from .import views
from .forms import NewUserForm
from django.contrib.auth import authenticate, login, logout
from django.template.context_processors import csrf
from django.utils.datastructures import MultiValueDictKeyError
from django.core.paginator import  Paginator, InvalidPage, EmptyPage, PageNotAnInteger



def LoginView(request):
    return render(request, 'index.html')



def LoginAction(request):
    if request.method == 'POST':
        username = request.POST.get("username")
        user = WikiNewsUser.objects.raw('select id, is_admin from wikinewsuser where username= %s',[username])
        for field in user:
            print(field.is_admin)
        if field.is_admin == True:
            return UserManagementView(request)
        else:
            return SearchView(request)
    return render(request, 'index.html')


def UserManagementView(request):
    userList = WikiNewsUser.objects.all()
    return render(request, 'user-management.html', {'data': userList})


def NewUserView(request):
    form = NewUserForm(request.POST)
    if request.method == 'POST':
        try:
            print(form.data)
            model = WikiNewsUser()
            model.username = form.data['username']
            model.password = form.data['password']
            try:
                is_admin = request.POST['isadmin']
            except MultiValueDictKeyError:
                is_admin = False
            if 'isadmin' in form.data:
                model.is_admin = True
            else:
                model.is_admin = False
            model.save()
            # return render(request, 'user-management.html')
        except:
           return HttpResponseRedirect('/user/usermanagement')
    return  HttpResponseRedirect('/user/usermanagement')


def SearchView(request):
    return render(request, 'search.html')

def LogoutView(request):
    return render(request, 'index.html')