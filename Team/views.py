from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required,user_passes_test
from U_Auth.models import User
from django.contrib import messages
from Core.models import Companies

# Create your views here.

######################### ADD TEAM MEMBER #########################

@user_passes_test(lambda u: u.is_staff)
def add_team_member(request):
    departments = Companies.objects.all()

    last_staff_id = User.objects.last()

    if last_staff_id:
        staff_id = f'STAFF0{last_staff_id.id+1}'
    else:
        staff_id = f'STAFF01'

    if request.method == 'POST':
        name = request.POST.get('name')
        image = request.FILES.get('image')

        if request.user.is_superuser:
            department_id = request.POST.get('department')
            department = Companies.objects.get(id=department_id)

        elif request.user.is_creatives_head:
            department = Companies.objects.get(id=1)
        elif request.user.is_technology_head:
            department = Companies.objects.get(id=2)
        elif request.user.is_academy_head:
            department = Companies.objects.get(id=3)
        
        job_role = request.POST.get('job-role')
        mobile = request.POST.get('mobile')
        email = request.POST.get('email')
        username = request.POST.get('username')
        password = request.POST.get('password')

        try:
            user = User.objects.create(first_name=name,username=username,Image=image,Department=department,
                                Job_Role=job_role,Mobile=mobile,email=email,Staff_ID=staff_id)

            user.save()
            user.set_password(password)
            user.save()

            messages.success(request,f'New Team member {name} added successfully ... !')

            return redirect('manage-team')
        
        except Exception as exception:
            messages.warning(request,exception)
            return redirect('add-team-member')

    context = {
        'page' : 'team',
        'staff_id' : staff_id,
        'departments' : departments
    }
    return render(request,'Dashboard/Team/add-team-member.html',context)

######################### MANAGE TEAM #########################

@user_passes_test(lambda u: u.is_staff)
def manage_team(request):

    if request.user.is_superuser:
        members = User.objects.filter(is_staff = False).order_by('-id')
    elif request.user.is_academy_head:
        members = User.objects.filter(is_staff = False , Department='Thycha Academy').order_by('-id')
    elif request.user.is_creatives_head:
        members = User.objects.filter(is_staff = False , Department='Thycha Creatives').order_by('-id')
    elif request.user.is_technology_head:
        members = User.objects.filter(is_staff = False , Department='Thycha Technologies').order_by('-id')

    if request.method == 'POST':
        member_id = request.POST.get('member_id')
        member = User.objects.get(id=member_id)
        member.delete()

        return redirect('manage-team')

    context = {
        'page' : 'team',
        'members' : members
    }
    return render(request,'Dashboard/Team/manage-team.html',context)

######################### MANAGE TEAM #########################

@user_passes_test(lambda u: u.is_staff)
def edit_team_member(request,staff_id):
    departments = Companies.objects.all()
    member = User.objects.get(id=staff_id)

    if request.method == 'POST':
        try:
            if len(request.FILES) > 0:
                member.Image = request.FILES.get('image')

            if request.user.is_superuser:
                department_id = request.POST.get('department')
                department = Companies.objects.get(id=department_id)
                member.Department = department
                
            member.first_name = request.POST.get('name')
            member.Job_Role = request.POST.get('job-role')
            member.Mobile = request.POST.get('mobile')
            member.email = request.POST.get('email')
            member.save()

            messages.success(request,'Team member details edited successfully ... !')
            return redirect('manage-team')
        
        except Exception as exception:
            messages.warning(request,exception)
            return redirect('edit-team-member',staff_id=member.id)

    context = {
        'page' : 'team',
        'member' : member,
        'departments' : departments
    }
    return render(request,'Dashboard/Team/edit-team-member.html',context)

######################### VIEW TEAM MEMBER #########################

@user_passes_test(lambda u: u.is_staff)
def view_team_member(request,staff_id):
    member = User.objects.get(id=staff_id)
    context = {
        'page' : 'team',
        'member' : member
    }
    return render(request,'Dashboard/Team/view-team-member.html',context)