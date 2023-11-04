from django.db import models

# Create your models here.

class Client(models.Model):
    Status = models.IntegerField(default=1)
    Name = models.CharField(max_length=100)
    Phone = models.CharField(max_length=20,null=True)
    Email = models.EmailField(null=True)
    Client_ID = models.CharField(max_length=25)

    def __str__(self):
        return self.Name