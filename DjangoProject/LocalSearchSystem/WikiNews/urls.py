from django.urls import path
from .import views

app_name = 'WikiNews'

urlpatterns = [
    path('item-management/', views.ItemManagementView, name='itemmanagement'),
    path('web-scrapping/', views.WebScrappingView, name = "webscrapping"),
    path('Item-details/', views.ItemDetailView, name = "itemdetails")
]