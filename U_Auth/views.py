from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required

# Create your views here.

#------------------------------------------------- SIGN IN ---------------------------------------------------#

def sign_in(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('dashboard')
        else:
            messages.error(request,'incorrect username or password')
            return redirect('.')
    return render(request,'Dashboard/Auth/sign-in.html')

#------------------------------------------------- EDIT PROFILE --------------------------------------------------#

@login_required
def edit_profile(request):
    if request.method == 'POST':
        if len(request.FILES) > 0:
            request.user.Image = request.FILES.get('image')
        request.user.first_name = request.POST.get('name')
        request.user.Mobile = request.POST.get('mobile')
        request.user.email = request.POST.get('email')

        request.user.save()

        messages.success(request,'Profile updated successfully ... !')
        return redirect('edit-profile')
    return render(request,'Dashboard/Auth/profile.html')


#----------------------------------------------CHANGE PASSWORD -----------------------------------------------#

@login_required
def changepassword(request):
    user = request.user
    if request.method == 'POST':
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')
        if password1 != password2:
            messages.warning(request,'password does not matching')
            return redirect('/change-password/')
        else:
            user.set_password(password1)
            user.save()
            return redirect('dashboard')
    return render(request,'Dashboard/Auth/change-password.html')

#------------------------------------------------- SIGN OUT --------------------------------------------------#

@login_required
def signout(request):
    logout(request)
    return redirect('sign-in')