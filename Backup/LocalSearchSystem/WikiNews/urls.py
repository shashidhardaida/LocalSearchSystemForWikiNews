from django.urls import path
from .import views

app_name = 'WikiNews'

urlpatterns = [
    path('item-management/', views.ItemManagementView, name='itemmanagement'),
    path('web-scrapping/', views.WebScrappingView, name = "webscrapping"),
    path('itemdetails/<int:itemId>', views.ItemDetailView, name = "itemdetails"),
    path('search-result/', views.SearchResultView, name = "searchresult"),
    path('search-item-result/', views.SearchItemResultView, name='searchitemresult'),
    path('scrapping/', views.ScrapWikiNews, name='scrapping'),
    path('item/del/<int:itemId>',views.DelItem)

]