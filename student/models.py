from django.db import models

# Create your models here.
class Student(models.Model):
    first_name= models.CharField(
    max_length=12)
    last_name=models.CharField(
    max_length=10)
    Age= models.PositiveSmallIntegerField()
    Date_of_birth= models.DateField()
            
        