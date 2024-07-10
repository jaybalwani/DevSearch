from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request):
    return HttpResponse('Home')

def projects(request):
    return render(request, 'projects/projects.html')

def project(request, pk):
    return render(request, 'projects/single-project.html', {'pk':pk})