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
    isadmin = forms.BooleanField(label='editisadmin')



class EditUserForm(forms.Form):
    edituserid = forms.IntegerField(label='edituserid')
    editusername = forms.CharField(label='editusername' ,max_length=255)
    editpassword = forms.CharField(widget=forms.PasswordInput(), max_length=100)
    editisadmin = forms.BooleanField(label='editisadmin')




class UserLoginForm(forms.Form):
    username = forms.CharField(label='User Name',max_length=100, required=True)
    password = forms.CharField(label='Password', widget=forms.PasswordInput(), max_length=100,required=True)

    # class Meta:
    #     model = WikiNewsUser
    #     fields = ['username', 'password']

    def clean(self):
        super(UserLoginForm, self).clean()
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')
        user = WikiNewsUser.objects.filter(username=username, password=password)
        print(len(user))
        print(user)
        if len(user) == 0:
            self._errors['password'] = self.error_class(['Invalid username or password'])
        else:
            return self.cleaned_data

