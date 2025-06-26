from django.db import models
from django.contrib.auth.models import User, Group


# Create your models here.

class Department(models.Model):
    DepartmentId=models.AutoField(primary_key=True)
    DepartmentName=models.CharField(max_length=100)
    ConsultationFees=models.IntegerField()
    
    def __str__(self):
        return self.DepartmentName
    
class Doctor(models.Model):
    DoctorId=models.AutoField(primary_key=True)
    DoctorName=models.CharField(max_length=100)
    Contact=models.CharField(max_length=10)
    EmailId=models.CharField(max_length=100)
    DOB=models.DateField(max_length=100)
    Address=models.CharField(max_length=100)
    SexChoices=[
        ('Male','Male'),
        ('Female','Female'),
        ('Other','Other')
    ]
    Sex=models.CharField(max_length=100)
    BloodGroup=models.CharField(max_length=5)
    Salary=models.IntegerField()
    DateOfJoining=models.DateField(max_length=100)
    DeptId=models.ForeignKey(Department, on_delete=models.CASCADE)
    Qualificatons=models.CharField(max_length=100)
    Availablility=models.BooleanField(default=True)

    def __str__(self):
        return self.DoctorName
