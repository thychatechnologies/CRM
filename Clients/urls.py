from django.urls import path
from Clients import views

urlpatterns = [
    path('add/',views.add_client,name='add-client',),
    path('manage/',views.manage_clients,name='manage-clients'),
    path('edit/<str:client_id>/',views.edit_client,name='edit-client'),
]