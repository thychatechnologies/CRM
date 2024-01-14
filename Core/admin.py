from django.contrib import admin
from Core.models import Companies

# Register your models here.

@admin.register(Companies)
class CompaniesModelAdmin(admin.ModelAdmin):
    list_display = ['Name','id']