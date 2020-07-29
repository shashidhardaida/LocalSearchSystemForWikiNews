from django.contrib.auth import authenticate
from django.contrib.auth.password_validation import validate_password
from django.core import exceptions
from django.core.validators import validate_email
from django.forms import ModelForm
from django import  forms
from .models import  WikiNewsUser
from django.contrib.auth.forms import ReadOnlyPasswordHashField




class NewUserForm(forms.Form):
    username = forms.CharField(label='username' ,max_length=255)
    password = forms.CharField(widget=forms.PasswordInput(), max_length=100)
    password2 = forms.CharField(widget=forms.PasswordInput(), max_length=100)
    isadmin = forms.BooleanField(label='isadmin')



class UserLoginForm(forms.Form):
    username = forms.CharField(max_length=30)
    password = forms.CharField(widget=forms.PasswordInput())

    def clean(self):
        users = WikiNewsUser.objects.filter(username=self.cleaned_data['username'])
        user = authenticate(username = self.cleaned_data['username'], password=self.cleaned_data['password'])
        if len(users) == 0 and user is None:
            raise forms.ValidationError("Invalid username or password. Please try again!")
        return self.cleaned_data

    def login(self, request):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')
        user = authenticate(username=username, password=password)
        return user