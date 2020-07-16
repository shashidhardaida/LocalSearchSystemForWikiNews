from django.shortcuts import render

# Create your views here.

def ItemManagementView(request):
    return render(request, 'item-management.html')
