from django.http import HttpResponse
from .models import Project, Task
from django.shortcuts import get_object_or_404, render, redirect
from .forms import CreateNewTask,CreateNewProject

# Create your views here.
def index(request):
    title = 'Django Course!'
    return render(request, 'index.html', {
        'title': title
    })

def about(request):
    username = 'Rafael'
    return render(request, 'about.html', {
        'username': username
    })

def hello(request, username):
    return HttpResponse("<h1>Hello %s</h1>" % username)

def project(request):
    # projects = list(Project.objects.values())
    projects = Project.objects.all()
    return render(request, 'projects/project.html', {
        'projects': projects
    })

def task(request):
    # task = Task.objects.get(id=id)
    # get_object_or_404(Task, id=id)
    tasks = Task.objects.all()
    return render(request, 'tasks/task.html', {
        'tasks': tasks
    })

def create_task(request):
    if request.method == 'GET':
        return render(request, 'tasks/create_task.html', {
            'form': CreateNewTask
        })
    else:
        Task.objects.create(title=request.POST['title'],
        description=request.POST['description'], project_id=2)
        return redirect('tasks')
    
def create_project(request):
    if request.method == 'GET':
        return render(request, 'projects/create_project.html', {
            'form': CreateNewProject()
        })
    else:
        Project.objects.create(name=request.POST["name"])
        return redirect('projects')
    
def project_detail(request, id):
    project = get_object_or_404(Project, id=id)
    tasks = Task.objects.filter(project_id=id)
    return render(request, 'projects/detail.html', {
        'project': project,
        'tasks': tasks
    })