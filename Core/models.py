from django.db import models

# Create your models here.

class Companies(models.Model):
    Name = models.CharField(max_length=100)

    def __str__(self):
        return self.Name