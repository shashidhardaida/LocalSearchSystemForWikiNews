from django.shortcuts import render

# Create your views here.

def ItemManagementView(request):
    return render(request, 'item-management.html')

def WebScrappingView(request):
    return render(request, 'web-scrapping.html')

def ItemDetailView(request):
    return render(request, 'details.html')

def SearchView(request):
    return render(request, 'search.html')
