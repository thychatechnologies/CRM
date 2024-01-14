from django.contrib import admin
from Tasks.models import Task

# Register your models here.

@admin.register(Task)
class TaskModelAdmin(admin.ModelAdmin):
    list_display = ['Title','Client','Assigned_By','Assigned_To','Priority','Start_Date','Due_Date']