from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Project, Review, Tag
from .forms import ProjectForm

# Create your views here.
def projects(request):
    projects = Project.objects.all()
    
    context = { 'projects': projects}
    return render(request, 'projects.html', context)

def project(request, pk):
    projectobj = Project.objects.get(id=pk)
    tags = projectobj.tags.all()
    context = { 'project': projectobj, 'tags': tags}
    return render(request, 'single-project.html', context)

def addproject(request):
    form = ProjectForm()
    if request.method == "POST":
        form = ProjectForm(request.POST)
        form.save()
        return redirect('projects')
    context = {'form': form}
    return render(request, 'project_form.html', context)

def editproject(request, pk):
    project = Project.objects.get(id=pk)
    form = ProjectForm(instance = project)

    if request.method == "POST":
        form = ProjectForm(request.POST, instance = project)
        form.save()
        return redirect('projects')
    context = {'form': form}
    return render(request, 'project_form.html', context)

def deleteproject(request , pk):
    project = Project.objects.get(id=pk)
    
    if request.method == "POST":
        project.delete()
        return redirect('projects')
    context = {'object': project}
    return render(request, 'delete_project.html', context)
    