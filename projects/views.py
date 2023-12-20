from django.shortcuts import render
from django.http import HttpResponse
from .models import Project, Review, Tag

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