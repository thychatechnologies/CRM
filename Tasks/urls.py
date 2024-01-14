from django.urls import path
from Tasks import views

urlpatterns = [
    path('',views.my_tasks,name='tasks'),
    path('create/',views.create_task,name='create-task'),
    path('delete/',views.delete_task,name='delete-task'),
    path('view/',views.task_view,name='task-view'),
    path('edit/<str:task_id>/',views.edit_task,name='edit-task'),
]