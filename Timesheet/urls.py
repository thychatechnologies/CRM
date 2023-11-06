from django.urls import path
from Timesheet import views

urlpatterns = [
    path('timesheet/',views.timesheet,name='timesheet'),
    path('add-timesheet/',views.add_timesheet,name='add-timesheet'),
    path('delete-timesheet/',views.delete_timesheet,name='delete-timesheet'),
    path('approve-timesheet/',views.approve_timesheet,name='approve-timesheet'),
    path('approve/',views.approve,name='approve'),
    path('reject/',views.reject,name='reject'),
    path('filter-timesheet/',views.filter_timesheet,name='filter-timesheet')
]