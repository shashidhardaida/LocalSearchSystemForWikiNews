from django.urls import path
from .import views

app_name = 'WikiNews'

urlpatterns = [
    path('wikinews/itemmanagement', views.ItemManagementView, name='itemmanagement'),
    # path('usermanagement/', views.UserManagementView, name = "usermanagement"),

]