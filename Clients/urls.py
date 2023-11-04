from django.urls import path
from Clients import views

urlpatterns = [
    path('add-client/',views.add_client,name='add-client',),
    path('manage-clients/',views.manage_clients,name='manage-clients'),
    path('edit-client/<str:client_id>/',views.edit_client,name='edit-client'),
]