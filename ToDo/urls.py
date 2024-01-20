from django.urls import path
from ToDo import views

urlpatterns = [
    path('',views.todo,name='todo'),
    path('add/',views.add_todo,name='add-todo'),
    path('delete/',views.delete_todo,name='delete-todo'),
    path('complete/',views.todo_complete,name='todo-complete')
]