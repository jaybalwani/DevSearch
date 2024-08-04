from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Project
from .forms import ProjectForm
from django.contrib.auth.decorators import login_required
from .utilities import searchProjects, paginateProjects

# Create your views here.

def home(request):
    return render(request, 'projects/index.html')

def projects(request):
    search_query, projects = searchProjects(request)
    projects, custom_range = paginateProjects(request, projects)
    return render(request, 'projects/projects.html', {'projects': projects,
                                                       'search_query': search_query,
                                                         'custom_range': custom_range})

def project(request, pk):
    project = Project.objects.get(id=pk)
    tags = project.tags.all()
    return render(request, 'projects/single-project.html', {'project':project, 'tags':tags})

@login_required(login_url='login')
def createProject(request):
    profile = request.user.profile
    form = ProjectForm()

    if request.method == 'POST':
        form = ProjectForm(request.POST, request.FILES)
        if form.is_valid():
            project = form.save(commit=False)
            project.owner = profile
            project.save()
            return redirect('account')

    context = {'form': form}
    return render(request, 'projects/project_form.html', context)

@login_required(login_url='login')
def updateProject(request, pk):
    profile = request.user.profile
    project = profile.project_set.get(id=pk)
    form = ProjectForm(instance=project)

    if request.method == 'POST':
        form = ProjectForm(request.POST, request.FILES, instance=project)
        if form.is_valid():
            form.save()
            return redirect('projects')

    context = {'form': form}
    return render(request, 'projects/project_form.html', context)

@login_required(login_url='login')
def deleteProject(request, pk):
    profile = request.user.profile
    project = profile.project_set.get(id=pk)
    context = {'object':project}

    if request.method == 'POST':
        project.delete()
        return redirect('projects')

    return render(request, 'delete_object.html', context)