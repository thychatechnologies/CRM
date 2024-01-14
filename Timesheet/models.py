from django.db import models
from U_Auth.models import User
from Clients.models import Client
from Tasks.models import Task
from datetime import datetime

# Create your models here.
STATUS = (
    ('Pending', 'Pending'),
    ('Rejected', 'Rejected'),
    ('Approved', 'Approved'),
    ('Reviced', 'Reviced'),
)

LOCATION = (
    ('Work from Office', 'Work from Office'),
    ('Work from Home', 'Work from Home'),
)

MODE = (
    ('New', 'New'),
    ('Rework', 'Rework'),
    ('Edit', 'Edit'),
)

TYPE = (
    ('Other', 'Other'),
    ('Poster', 'Poster'),
    ('Video', 'Video'),
    ('Branding', 'Branding'),
    ('Brochure', 'Brochure'),
    ('Packaging', 'Packaging'),
    ('Developing', 'Developing'),
)

class Time_Sheet(models.Model):
    Added_By = models.ForeignKey(User,on_delete=models.SET_NULL,null=True)
    Status = models.CharField(max_length=100, choices=STATUS, default='Pending')

    Date = models.DateField()
    Start_Time = models.TimeField()
    End_Time = models.TimeField()

    Location = models.CharField(max_length=25,choices=LOCATION)
    Mode = models.CharField(max_length=100, choices=MODE)
    Type = models.CharField(max_length=100, choices=TYPE)
    Client = models.ForeignKey(Client, on_delete=models.SET_NULL,null=True)  
    Task = models.ForeignKey(Task,on_delete=models.DO_NOTHING)
    Remarks = models.TextField()
    Duration = models.DurationField(null=True, blank=True)

    def __str__(self):
        return f"{self.Added_By} - {self.Date}"

    def save(self, *args, **kwargs):
        if self.Start_Time and self.End_Time:
            start_time = datetime.strptime(str(self.Start_Time), '%H:%M:%S').time()
            end_time = datetime.strptime(str(self.End_Time), '%H:%M:%S').time()

            start_datetime = datetime.combine(self.Date, start_time)
            end_datetime = datetime.combine(self.Date, end_time)
            duration = end_datetime - start_datetime

            self.Duration = duration

        super(Time_Sheet, self).save(*args, **kwargs)

    def formatted_duration(self):
        hours, remainder = divmod(self.Duration.seconds, 3600)
        minutes, _ = divmod(remainder, 60)
        return f"{hours} hr and {minutes}m"
    
class Filter(models.Model):
    Employee = models.ForeignKey(User,on_delete=models.SET_NULL,null=True)
    From_Date = models.DateField(null=True)
    To_Date = models.DateField(null=True)
    Status = models.CharField(max_length=50,default='Pending')
    Client = models.ForeignKey(Client,on_delete=models.SET_NULL,null=True)
    Task = models.ForeignKey(Task,on_delete=models.SET_NULL,null=True)