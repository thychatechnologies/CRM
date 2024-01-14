from django.db import models
from Clients.models import Client
from U_Auth.models import User

# Create your models here.

PRIORITY = (
    ('Normal', 'Normal'),
    ('Medium', 'Medium'),
    ('High', 'High'),
)

class Task(models.Model):
    Added_Date = models.DateField(auto_now_add=True)
    Status = models.IntegerField(default=1)
    
    Client = models.ForeignKey(Client,on_delete=models.CASCADE)
    Assigned_By = models.ForeignKey(User,on_delete=models.CASCADE,related_name='assigned_by')
    Assigned_To = models.ForeignKey(User,on_delete=models.CASCADE,related_name='assigned_to')
    Title = models.CharField(max_length=250)
    Description = models.TextField()
    Priority = models.CharField(max_length=50,choices=PRIORITY, default='Normal')
    Start_Date = models.DateField(null=True)
    Due_Date = models.DateField(null=True)

    def __str__(self):
        return self.Title