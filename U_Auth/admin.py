from django.contrib import admin
from U_Auth.models import User

# Register your models here.

@admin.register(User)
class UserModelAdmin(admin.ModelAdmin):
    list_display = [
        'id','username','is_superuser','is_staff','is_academy_head','is_creatives_head','is_technology_head',
        'first_name','Mobile','email','Staff_ID','Department','Job_Role']