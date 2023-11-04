from django.shortcuts import render
from django.contrib.auth.decorators import login_required,user_passes_test

# Create your views here.

@user_passes_test(lambda u: u.is_superuser)
def create_project(request):
    return render(request,'Dashboard/Project/create-project.html')