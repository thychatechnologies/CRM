from django.urls import path
from Team import views

urlpatterns = [
    path('add/',views.add_team_member,name='add-team-member'),
    path('manage/',views.manage_team,name='manage-team'),
    path('edit/<str:staff_id>/',views.edit_team_member,name='edit-team-member'),
    path('view/<str:staff_id>/',views.view_team_member,name='view-team-member'),
]