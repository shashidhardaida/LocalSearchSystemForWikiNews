from django.urls import path, include
from .import views

app_name = 'WikiNews'

urlpatterns = [
    path('item-management/', views.ItemManagementView, name='itemmanagement'),
    path('web-scrapping/', views.WebScrappingView, name = "webscrapping"),
    path('itemdetails/<int:itemId>', views.ItemDetailView, name = "itemdetails"),
    path('scrapping/', views.ScrapWikiNews, name='scrapping'),
    path('item/del/<int:itemId>',views.DelItem),
    path('search/', include('haystack.urls')),

]