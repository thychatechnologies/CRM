from django.urls import path
from Projects import views

urlpatterns = [
    path('create/',views.create_project,name='create-project')
]