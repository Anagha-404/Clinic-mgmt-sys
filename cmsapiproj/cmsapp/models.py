from django.db import models
from django.contrib.auth.models import User, Group
from django.utils import timezone
import datetime


# Create your models here.

class Department(models.Model):
    DepartmentId=models.AutoField(primary_key=True)
    DepartmentName=models.CharField(max_length=100)
    ConsultationFees=models.IntegerField()
    
    def _str_(self):
        return self.DepartmentName
    
class Doctor(models.Model):
    DoctorId=models.AutoField(primary_key=True)
    DoctorName=models.CharField(max_length=100)
    Contact=models.CharField(max_length=10)
    Email=models.EmailField(max_length=100)
    DOB=models.DateField()
    Address=models.CharField(max_length=100)
    SexChoices=[
        ('Male','Male'),
        ('Female','Female'),
        ('Other','Other')
    ]
    Sex=models.CharField(max_length=10, choices=SexChoices)
    BloodGroup=models.CharField(max_length=5)
    Salary=models.IntegerField()
    DateOfJoining=models.DateField()
    DeptId=models.ForeignKey(Department, on_delete=models.CASCADE)
    Qualifications =models.CharField(max_length=100)
    Availablility=models.BooleanField(default=True)

    def _str_(self):
        return self.DoctorName
    
class Patient(models.Model):
    PatientId = models.AutoField(primary_key=True)
    Name = models.CharField(max_length=100)
    Email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=15, unique=True)
    Address = models.TextField()
    Gender = models.CharField(max_length=10)
    BloodGroup = models.CharField(max_length=10)
    Age = models.IntegerField()

    def _str_(self):
        return self.Name

class Appointment(models.Model):
    AppointmentId = models.AutoField(primary_key=True)
    PatientId = models.ForeignKey(Patient,on_delete=models.CASCADE)
    DoctorId = models.ForeignKey(Doctor,on_delete=models.CASCADE)
    AppointmentDate = models.DateField()
    AppointmentTime = models.TimeField( choices=[(datetime.time(10, 0), '10:00 AM'),
                                                             (datetime.time(10, 30), '10:30 AM'),
                                                             (datetime.time(11, 0), '11:00 AM'),
                                                             (datetime.time(11, 30), '11:30 AM'),
                                                             (datetime.time(12, 0), '12:00 PM'),
                                                             (datetime.time(12, 30), '12:30 PM'),
                                                             (datetime.time(13, 30), '01:30 PM'),
                                                             (datetime.time(14, 0), '02:00 PM'),
                                                             (datetime.time(14, 30), '02:30 PM'),
                                                             (datetime.time(15, 0), '03:00 PM'),
                                                             (datetime.time(15, 30), '03:30 PM'),
                                                             (datetime.time(16, 0), '04:00 PM'),
                                                             (datetime.time(16, 30), '04:30 PM'),
                                                             (datetime.time(17, 0), '05:00 PM'),])
    Status = models.CharField(max_length=20, choices=[('Scheduled', 'Scheduled'), ('Completed', 'Completed'), ('Cancelled', 'Cancelled')])

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['DoctorId', 'AppointmentDate', 'AppointmentTime'],
                name='unique_doctor_date_time'
            ),

            models.UniqueConstraint(
                fields=['PatientId', 'AppointmentDate', 'AppointmentTime'],
                name='unique_patient_date_time'
            )]
    def _str_(self):
        return self.Status

class Medicine(models.Model):
    MedicineId=models.AutoField(primary_key=True)
    MedicineName=models.CharField(max_length=100)

    def _str_(self):
        return self.MedicineName
    
class LabTest(models.Model):
    LabTestId=models.AutoField(primary_key=True)
    TestName=models.CharField(max_length=200)
    TestDescription=models.CharField(max_length=300)

    def _str_(self):
        return self.TestName

class Prescription(models.Model):
    AppointmentId=models.ForeignKey(Appointment, on_delete=models.CASCADE)
    DoctorId=models.ForeignKey(Doctor, on_delete=models.CASCADE)
    MedicineId=models.ForeignKey(Medicine, on_delete=models.CASCADE)
    DateIssued=models.DateField()
    LabTestId=models.ForeignKey(LabTest, on_delete=models.CASCADE)
    Description=models.CharField(max_length=200)

    def _str_(self):
        return self.Description
    
class UserDetails(models.Model):
    User = models.OneToOneField(User, on_delete=models.CASCADE,related_name='user_details')
    Name = models.CharField(max_length=100)

    def _str_(self):
        return self.Name

class Receptionist(models.Model):
    ReceptionistId = models.AutoField(primary_key=True)
    Name = models.CharField(max_length=100)
    Email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=15, unique=True)

    def _str_(self):
        return self.Name