from django.shortcuts import render,redirect
from Clients.models import Client
from django.contrib import messages
from django.contrib.auth.decorators import login_required,user_passes_test

# Create your views here.

######################### ADD CLIENTS #########################

@user_passes_test(lambda u: u.is_staff)
def add_client(request):
    client = Client.objects.last()
    
    if client:
        client_id = f'CLIENT-0{client.id+1}'
    else:
        client_id = f'CLIENT-01'

    if request.method == 'POST':
        name = request.POST.get('name')
        mobile = request.POST.get('mobile')
        email = request.POST.get('email')

        try:
            Client.objects.create(Name=name,Phone=mobile,Email=email,Client_ID=client_id)
            messages.success(request,'New client added successfully ...!')
            return redirect('manage-clients')
        
        except Exception as exception:
            messages.warning(request,exception)
            return redirect('add-client')

    context = {
        'page' : 'clients',
        'client_id' : client_id
    }
    return render(request,'Dashboard/Clients/add-client.html',context)

######################### MANAGE CLIENTS #########################

@user_passes_test(lambda u: u.is_staff)
def manage_clients(request):
    clients = Client.objects.filter(Status=1).order_by('Name')

    if request.method == 'POST':
        client_id = request.POST.get('client_id')
        client = Client.objects.get(id=client_id)
        client.Status = 0
        client.save()
        return redirect('manage-clients')

    context = {
        'page' : 'clients',
        'clients' : clients
    }
    return render(request,'Dashboard/Clients/manage-clients.html',context)

######################### EDIT CLIENT #########################

@user_passes_test(lambda u: u.is_staff)
def edit_client(request,client_id):
    client = Client.objects.get(id=client_id)

    if request.method == 'POST':
        try:
            client.Name = request.POST.get('name')
            client.Phone = request.POST.get('mobile')
            client.Email = request.POST.get('email')
            client.save()

            messages.success(request,'Client details edited successfully .... !')
            return redirect('manage-clients')
        
        except Exception as exception:
            messages.warning(request,exception)
            return redirect('edit-client' , client_id=client.id)
        
    context = {
        'page' : 'clients',
        'client' : client
    }
        
    return render(request,'Dashboard/Clients/edit-client.html',context)