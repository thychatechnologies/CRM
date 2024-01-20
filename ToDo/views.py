from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from ToDo.models import Todo
from django.http import JsonResponse

# Create your views here.

@login_required
def todo(request):
    todos = Todo.objects.filter(Added_By=request.user).order_by('-Date')
    context = {
        'page' : 'todo',
        'todos' : todos
    }
    return render(request,'Dashboard/ToDo/todo.html',context)

@login_required
def add_todo(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        Todo.objects.create(Title=title,Added_By=request.user)

        return redirect('todo')
    
@login_required
def delete_todo(request):
    if request.method == 'POST':
        todo_id = request.POST.get('todo_id')
        todo = Todo.objects.get(id=todo_id)
        todo.delete()
        return redirect('todo')
    
@csrf_exempt
def todo_complete(request):
    if request.method == 'POST':
        todo_id = request.POST.get('todo_id')
        todo = Todo.objects.get(id=todo_id)
        todo.Status = not todo.Status
        todo.save()

        return JsonResponse({'status' : 'success'})