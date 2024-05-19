from django.shortcuts import render, redirect 
from rest_framework import generics
import requests


def home(request):
    return render(request, 'task-list.html')

# Create your views here.

#def apinikal(request):
    # Define the API endpoint
#    api_url = 'http://127.0.0.1:8000/title'
#
#     try:
#       # Make a GET request to the API
#       response = requests.get(api_url)
#        if response.status_code == 200:  # <- Corrected indentation here
#            data = response.json()
#            context = {'api_data': data}
#            return render(request, 'task-list.html', context)


# views.py

def data_view(request):
    # Fetch data from API
    api_url = 'http://127.0.0.1:8001/titles/'
    response = requests.get(api_url)
    data = response.json()
    
    # Pass data to template context
    context = {'data': data}
    
    # Render template with data
    return render(request, 'task-details.html', context)

def userapi(request):
    api_url = 'http://127.0.0.1:8001/users/'
    response = requests.get(api_url)
    data = response.json()
    context =  {'userdata':data} 
    return render(request, 'home.html', context)     

def ownerapi(request):
    api_url = "http://127.0.0.1:8001/owners/"
    response = requests.get(api_url)
    ownerdata = response.json()
    context = {'ownerdata':ownerdata}
    return render(request,  'home.html', context)

def propertyapi(request):
    api_url = "http://127.0.0.1:8001/properties"
    response = requests.get(api_url)
    propertydata = response.json()
    context = {'propertydata':propertydata}
    return render(request, home.html, context)



from .forms import TitleForm

def add_title(request):
    if request.method == 'POST':
        form = TitleForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('data')  # redirect to a page showing a list of titles
    else:
        form = TitleForm()
    return render(request, 'add-title.html', {'form': form})
