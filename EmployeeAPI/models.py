from django.db import models

# Create your models here.

class Employees(models.Model):
    emp_id = models.CharField(max_length=10)
    name = models.CharField(max_length=20)
    desc = models.CharField(max_length=50)
    
    def __str__(self):
        return self.name
    