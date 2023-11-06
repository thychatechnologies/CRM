from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from Clients.models import Client
from Timesheet.models import Time_Sheet
from datetime import datetime,time
from django.db.models import Q, F, Sum
from django.contrib import messages
from U_Auth.models import User
from django.core import serializers

today = datetime.today()

# Create your views here.

def format_duration(duration):
    hours, remainder = divmod(duration.seconds, 3600)
    minutes, _ = divmod(remainder, 60)
    return f"{hours} hr and {minutes}m"

@login_required
def timesheet(request):

                                        #GET

    projects = Client.objects.all()
    timesheets = Time_Sheet.objects.filter(Added_By=request.user,Date=today).order_by('-id')

    objects = Time_Sheet.objects.filter(Added_By=request.user).order_by('-id')

    pending = objects.filter(Status='Pending',Date=today).aggregate(
        total_duration=Sum(F('End_Time') - F('Start_Time'))
    )['total_duration']

    pending_month = timesheets.filter(Status='Pending',Date__month=today.month).aggregate(
        total_duration=Sum(F('End_Time') - F('Start_Time'))
    )['total_duration']

    approved = objects.filter(Status='Approved',Date=today).aggregate(
        total_duration=Sum(F('End_Time') - F('Start_Time'))
    )['total_duration']

    approved_month = timesheets.filter(Status='Approved',Date__month=today.month).aggregate(
        total_duration=Sum(F('End_Time') - F('Start_Time'))
    )['total_duration']

    rejected = objects.filter(Status='Rejected',Date=today).aggregate(
        total_duration=Sum(F('End_Time') - F('Start_Time'))
    )['total_duration']

    rejected_month = timesheets.filter(Status='Approved',Date__month=today.month).aggregate(
        total_duration=Sum(F('End_Time') - F('Start_Time'))
    )['total_duration']
    
    try:
        pending = format_duration(pending)
    except:
        pending = "00 hr and 00m"
    
    try:
        pending_month = format_duration(pending_month)
    except:
        pending_month = "00 hr and 00m"

    try:
        approved = format_duration(approved)
    except:
        approved = "00 hr and 00m"

    try:
        approved_month = format_duration(approved_month)
    except:
        approved_month = "00 hr and 00m"

    try:
        rejected = format_duration(rejected)
    except:
        rejected = "00 hr and 00m"

    try:
        rejected_month = format_duration(rejected_month)
    except:
        rejected_month = "00 hr and 00m"

    ##################################################################################################

                                        #POST

    if request.method == 'POST':
        start_time = request.POST.get('start_time')
        end_time = request.POST.get('end_time')
        location = request.POST.get('location')
        mode = request.POST.get('mode')
        type = request.POST.get('type')
        project_id = request.POST.get('project')
        project = Client.objects.get(id=project_id)
        remarks = request.POST.get('remarks')

        start_time = str(start_time) + ":00"
        end_time = str(end_time) + ":00"

        objects = Time_Sheet.objects.filter(Added_By=request.user,Date=today)

        start_overlapping = objects.filter(
            Q(Start_Time__lte=start_time) & Q(End_Time__gte=start_time)
        )

        end_overlapping = objects.filter(
            Q(Start_Time__lte=end_time) & Q(End_Time__gte=end_time)
        )

        if start_overlapping.exists() or end_overlapping.exists():

            # messages.warning(request,' invalid time slot cant add time sheet ...! ')
            return redirect('timesheet')
        
        else:
            Time_Sheet.objects.create(
                Added_By=request.user,Date=today,Start_Time=start_time,End_Time=end_time,Location=location,
                Mode=mode,Type=type,Client=project,Remarks=remarks
            )

            messages.success(request,' time sheet added successfully ...! ')
            return redirect('timesheet')
    
    context = {
        'page' : 'timesheet',
        'projects' : projects,
        'timesheets' : timesheets,

        'pending' : pending,
        'pending_month' : pending_month,

        'approved' : approved,
        'approved_month' : approved_month,

        'rejected' : rejected,
        'rejected_month' : rejected_month,
    }
    return render(request,'Dashboard/Timesheet/timesheet.html',context)

@csrf_exempt
def add_timesheet(request):
    if request.method == 'POST':
        start_time = request.POST.get('start_time')
        end_time = request.POST.get('end_time')
        location = request.POST.get('location')
        mode = request.POST.get('mode')
        type = request.POST.get('type')
        project_id = request.POST.get('project')
        project = Client.objects.get(id=project_id)
        remarks = request.POST.get('remarks')

        start_time = str(start_time) + ":00"
        end_time = str(end_time) + ":00"

        objects = Time_Sheet.objects.filter(Added_By=request.user)

        start_overlapping = objects.filter(
            Q(Start_Time__lte=start_time) & Q(End_Time__gte=start_time)
        )

        end_overlapping = objects.filter(
            Q(Start_Time__lte=end_time) & Q(End_Time__gte=end_time)
        )

        if start_overlapping.exists() or end_overlapping.exists():
            return JsonResponse({'response': 'failed'})
        else:
            time_sheet = Time_Sheet.objects.create(
                Added_By=request.user,Date=today,Start_Time=start_time,End_Time=end_time,Location=location,
                Mode=mode,Type=type,Client=project,Remarks=remarks
            )

            time_sheet_data = {
                'id': time_sheet.id,
                'Added_By': time_sheet.Added_By.username,
                # 'Date': time_sheet.Date.strftime('%Y-%m-%d'),
                # 'Start_Time': time_sheet.Start_Time.strftime('%H:%M:%S'),
                # 'End_Time': time_sheet.End_Time.strftime('%H:%M:%S'),
                'Location': time_sheet.Location,
                'Mode': time_sheet.Mode,
                'Type': time_sheet.Type,
                'Client': time_sheet.Client.Name,
                'Remarks': time_sheet.Remarks,
            }

            return JsonResponse({'response': 'success','time_sheet':time_sheet_data})

    return JsonResponse({'response': 'error'})

@login_required
def delete_timesheet(request):
    if request.method == 'POST':
        timesheet_id = request.POST.get('timesheet_id')
        timesheet = Time_Sheet.objects.get(id=timesheet_id)
        timesheet.delete()
        return redirect('timesheet')
    
@login_required
def approve_timesheet(request):
    timesheets = Time_Sheet.objects.filter(Status='Pending')
    members = User.objects.filter(Department='Thycha Creatives')
    clients = Client.objects.all().order_by('Name')
    context = {
        'page' : 'approve-timesheet',
        'timesheets' : timesheets,
        'members' : members,
        'clients' : clients
    }
    return render(request,'Dashboard/Timesheet/approve-timesheet.html',context)

@csrf_exempt
def approve(request):
    if request.method == 'POST':
        ts_id = request.POST.get('id')
        timesheet = Time_Sheet.objects.get(id=ts_id)
        timesheet.Status = 'Approved'
        timesheet.save()
        # return JsonResponse({'status':'approved'})
        return redirect('approve-timesheet')

@csrf_exempt
def reject(request):
    if request.method == 'POST':
        ts_id = request.POST.get('id')
        timesheet = Time_Sheet.objects.get(id=ts_id)
        timesheet.Status = 'Rejected'
        timesheet.save()
        # return JsonResponse({'status':'rejected'})
        return redirect('approve-timesheet')
    
@csrf_exempt
def filter_timesheet(request):
    timesheets = Time_Sheet.objects.filter(Status='Pending')
    timesheet_data = [{
        'id': timesheet.id,
        'Added_By' : timesheet.Added_By.first_name,
        'Client' : timesheet.Client.Name,
        'Location' : timesheet.Location,
        'Mode' : timesheet.Mode,
        'Date' : timesheet.Date,
        'Start_Time' : timesheet.Start_Time,
        'End_Time' : timesheet.End_Time,
        'Duration' : timesheet.formatted_duration(),
        'Remarks' : timesheet.Remarks,
        'Status' : timesheet.Status
        } for timesheet in timesheets]
    return JsonResponse({'status':'success','timesheets':timesheet_data})