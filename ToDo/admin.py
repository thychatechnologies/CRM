from django.contrib import admin
from ToDo.models import Todo

# Register your models here.

@admin.register(Todo)
class TodoModelAdmin(admin.ModelAdmin):
    list_display = ['Title','id','Date','Status']