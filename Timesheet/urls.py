from django.urls import path
from Timesheet import views

urlpatterns = [
    path('',views.timesheet,name='timesheet'),
    path('add/',views.add_timesheet,name='add-timesheet'),
    path('delete/',views.delete_timesheet,name='delete-timesheet'),
    path('approve-timesheet/',views.approve_timesheet,name='approve-timesheet'),
    path('approve/',views.approve,name='approve'),
    path('revice/',views.revice,name='revice'),
    path('reject/',views.reject,name='reject'),
    path('filter/',views.filter_timesheet,name='filter-timesheet'),
    path('get/tasks/',views.get_tasks,name='get-tasks'),
    path('reset/filter/',views.reset_filter,name='reset-filter')
]