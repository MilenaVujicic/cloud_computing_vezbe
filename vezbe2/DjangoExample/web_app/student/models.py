from django.db import models

# Create your models here.



class Student(models.Model):
    name = models.CharField(null=False, max_length=512)
    surname = models.CharField(null=False, max_length=512)
    avg_grade = models.DecimalField(null=False, max_digits=4, decimal_places=2)

