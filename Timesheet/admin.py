from django.contrib import admin
from Timesheet.models import Time_Sheet,Filter

# Register your models here.

@admin.register(Time_Sheet)
class TimeModelAdmin(admin.ModelAdmin):
    list_display = ['Added_By','Date','Start_Time','End_Time','Client','Remarks']

@admin.register(Filter)
class FilterModelAdmin(admin.ModelAdmin):
    list_display = ['Employee','Client','Task','Status','From_Date','To_Date']