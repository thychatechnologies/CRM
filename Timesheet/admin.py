from django.contrib import admin
from Timesheet.models import Time_Sheet

# Register your models here.

@admin.register(Time_Sheet)
class TimeModelAdmin(admin.ModelAdmin):
    list_display = ['Added_By','Date','Start_Time','End_Time','Client','Remarks']