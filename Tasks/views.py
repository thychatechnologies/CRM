from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from Tasks.models import Task
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from Clients.models import Client
from U_Auth.models import User
from django.contrib import messages

# Create your views here.

######################### CREATE TASK #########################

@login_required
def create_task(request):
    clients = Client.objects.all()
    employees = User.objects.all()

    if request.method == 'POST':
        title = request.POST.get('title')
        client_id = request.POST.get('client')
        employee_id = request.POST.get('employee')
        start_date = request.POST.get('start_date')
        due_date = request.POST.get('due_date')
        priority = request.POST.get('priority')
        description = request.POST.get('description')

        try:
            client = Client.objects.get(id=client_id)
            employee = User.objects.get(id=employee_id)

            Task.objects.create(
                Client=client,Assigned_By=request.user,Assigned_To=employee,
                Title=title,Description=description,Priority=priority,Start_Date=start_date,Due_Date=due_date
            )

            messages.success(request,'Task Created Successfully ... !')

            return redirect('tasks')
        
        except Exception as e:
            messages.warning(request,e)
            return redirect('create-task')

    context = {
        'page' : 'tasks',
        'clients' : clients,
        'employees' : employees
    }
    return render(request,'Dashboard/Tasks/create-task.html',context)

######################### MANAGE TASKS #########################

@login_required
def my_tasks(request):

    if request.user.is_superuser:
        tasks = Task.objects.all().filter(Status=1).order_by('-id')
    else:
        tasks = Task.objects.filter(Assigned_To=request.user).filter(Status=1).order_by('-id')

    context = {
        'page' : 'tasks',
        'tasks' : tasks
    }
    return render(request,'Dashboard/Tasks/my-tasks.html',context)

######################### EDIT TASK #########################

@login_required
def edit_task(request,task_id):
    clients = Client.objects.all()
    employees = User.objects.all()
    task = Task.objects.get(id=task_id)

    if request.method == 'POST':
        client_id = request.POST.get('client')
        employee_id = request.POST.get('employee')

        try:
            client = Client.objects.get(id=client_id)
            employee = User.objects.get(id=employee_id)

            task.Client = client
            task.Assigned_To = employee
            task.Title = request.POST.get('title')
            task.Description = request.POST.get('description')
            task.Priority = request.POST.get('priority')
            task.Start_Date = request.POST.get('start_date')
            task.Due_Date = request.POST.get('due_date')

            task.save()
            messages.success(request,'Task Edited Successfully ... !')
            return redirect('tasks')
        
        except Exception as exception:
            messages.warning(request,exception)
            return redirect('edit-task',task_id=task.id)

    context = {
        'page' : 'tasks',
        'clients' : clients,
        'employees' : employees,
        'task' : task
    }
    return render(request,'Dashboard/Tasks/edit-task.html',context)

######################### VIEW TASK #########################

@csrf_exempt
def task_view(request):
    task_id = request.POST.get('task_id')
    task = Task.objects.get(id=task_id)

    return JsonResponse({
        'status' : 'success',
        'title' : task.Title
    })

######################### DELETE TASK #########################

@login_required
def delete_task(request):
    task_id = request.POST.get('task_id')
    task = Task.objects.get(id=task_id)
    task.Status = 0
    task.save()
    return redirect('tasks')