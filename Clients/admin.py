from django.contrib import admin
from Clients.models import Client

# Register your models here.

@admin.register(Client)
class ClientModelAdmin(admin.ModelAdmin):
    list_display = ['id','Client_ID','Name','Phone','Email']