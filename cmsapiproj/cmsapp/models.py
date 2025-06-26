from django.db import models
from django.contrib.auth.models import User, Group

# Create your models here.
class Receptionist(models.Model):
    ReceptionistId = models.AutoField(primary_key=True)
    Name = models.CharField(max_length=100)
    Email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=15, unique=True)
    UserId =models.ForeignKey(User, on_delete=models.CASCADE)

    

class UserDetails(models.Model):
    UserId = models.AutoField(primary_key=True)
    Name = models.CharField(max_length=100)
    RoleId = models.ForeignKey(Group, on_delete=models.CASCADE)

    def __str__(self):
        return self.Name
    
class RoleDetails(models.model):
    RoleId = models.AutoField(primary_key=True)
    RoleName = models.CharField(max_length=50)

    def __str__(self):
        return self.RoleName
    


class Patient(models.Model):
    PatientId = models.AutoField(primary_key=True)
    Name = models.CharField(max_length=100)
    Email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=15, unique=True)
    Address = models.TextField()
    Gender = models.CharField(max_length=10)
    BloodGroup = models.CharField(max_length=10)
    Age = models.IntegerField()
    TokenId = models.ForeignKey(User, on_delete=models.CASCADE)


    def __str__(self):
        return self.Name
    
class Appointment(models.Model):
    AppointmentId = models.AutoField(primary_key=True)
    PatientId = models.ForeignKey(Patient,max_length=100)
    DoctorId = models.ForeignKey(Doctor,max_length=100)
    AppointmentDate = models.DateTimeField()
    AppointmentTime = models.ForeignKey()
    Status = models.CharField(max_length=20, choices=[('Scheduled', 'Scheduled'), ('Completed', 'Completed'), ('Cancelled', 'Cancelled')])
    ReceptionistId = models.ForeignKey(Receptionist, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.PatientName} - {self.DoctorName} on {self.AppointmentDate}"
    
    class Time(models.Model):
        TimeId = models.AutoField(primary_key=True)
        StartTime = models.TimeField()
        AppointmentId = models.ForeignKey(Appointment, on_delete=models.CASCADE)
        

       