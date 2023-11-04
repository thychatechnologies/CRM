from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator

# Create your views here.

#----------------------------------- DASHBOARD -----------------------------------#

@login_required
def dashboard(request):
    page = 'dashboard'

    context = {
        'page' : page
    }
    return render(request,'Dashboard/Core/dashboard.html',context)