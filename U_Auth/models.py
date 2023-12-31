from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class User(AbstractUser):
    Image = models.ImageField(null=True,upload_to='Team')
    Staff_ID = models.CharField(max_length=25)
    Department = models.CharField(max_length=100)
    Job_Role = models.CharField(max_length=100)
    Mobile = models.CharField(max_length=20)

    is_academy_head = models.BooleanField(default=False)
    is_creatives_head = models.BooleanField(default=False)
    is_technology_head = models.BooleanField(default=False)

    def __str__(self):
        return self.first_name