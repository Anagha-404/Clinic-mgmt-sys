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
    RoleId=models.ForeignKey(RoleDetails, on_delete=models.CASCADE)
    Contact=models.CharField(max_length=10)
    EmailId=models.CharField(max_length=100)
    DOB=models.DateField()
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

class Prescription(models.Model):
    AppointmentId=models.ForeignKey(Appointment, on_delete=models.CASCADE)
    DoctorId=models.ForeignKey(Doctor, on_delete=models.CASCADE)
    MedicineId=models.ForeignKey(Medicine, on_delete=models.CASCADE)
    DateIssued=models.DateField()
    LabTestId=models.ForeignKey(LabTest, on_delete=models.CASCADE)

class Medicine(models.Model):
    MedicineId=models.AutoField(primary_key=True)
    MedicineName=models.CharField(max_length=100)

    def __str__(self):
        return self.MedicineName
    
class LabTest(models.Model):
    LabTestId=models.AutoField(primary_key=True)
    TestName=models.CharField(max_length=200)
    TestDescription=models.CharField(max_length=300)

    def __str__(self):
        return self.TestName

class Receptionist(models.Model):
    ReceptionistId = models.AutoField(primary_key=True)
    Name = models.CharField(max_length=100)
    RoleId=models.ForeignKey(RoleDetails, on_delete=models.CASCADE)
    Email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=15, unique=True)
    UserId =models.ForeignKey(User, on_delete=models.CASCADE)

    
class UserDetails(models.Model):
    UserId = models.AutoField(primary_key=True)
    Name = models.CharField(max_length=100)
    RoleId = models.ForeignKey(Group, on_delete=models.CASCADE)

    def __str__(self):
        return self.Name
    
class RoleDetails(models.Model):
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

    def __str__(self):
        return self.Name
    
class Appointment(models.Model):
    AppointmentId = models.AutoField(primary_key=True)
    PatientId = models.ForeignKey(Patient,max_length=100)
    DoctorId = models.ForeignKey(Doctor,max_length=100)
    AppointmentDate = models.DateTimeField()
    AppointmentTime = models.ForeignKey(Time, on_delete=models.CASCADE)
    Status = models.CharField(max_length=20, choices=[('Scheduled', 'Scheduled'), ('Completed', 'Completed'), ('Cancelled', 'Cancelled')])
    ReceptionistId = models.ForeignKey(Receptionist, on_delete=models.CASCADE)

    def __str__(self):
        return self.AppointmentId
    
class Time(models.Model):
    AppointmentTime = models.TimeField(primary_key=True)
    AppointmentId = models.ForeignKey(Appointment, on_delete=models.CASCADE)
        

 