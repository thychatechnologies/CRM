from django.db import models
from U_Auth.models import User

# Create your models here.

class Todo(models.Model):
    Date = models.DateField(auto_now_add=True)
    Added_By = models.ForeignKey(User,on_delete=models.CASCADE)
    Title = models.CharField(max_length=225)
    Status = models.BooleanField(default=False)

    def __str__(self):
        return self.Title