from django.shortcuts import render
from .models import Department,Doctor,Prescription,Medicine,LabTest,Receptionist,UserDetails,Patient,Appointment
from .serializers import DepartmentSerializer,DoctorSerializer,PrescriptionSerializer,MedicineSerializer, LabTestSerializer,ReceptionistSerializer, UserDetailsSerializer,PatientSerializer,AppointmentSerializer
from rest_framework import viewsets

# Create your views here.

class DepartmentViewSet(viewsets.ModelViewSet):
    queryset=Department.objects.all()
    serializer_class=DepartmentSerializer

class DoctorViewSet(viewsets.ModelViewSet):
    queryset=Doctor.objects.all()
    serializer_class=DoctorSerializer

class PrescriptionViewSet(viewsets.ModelViewSet):
    queryset=Prescription.objects.all()
    serializer_class=PrescriptionSerializer

class MedicineViewSet(viewsets.ModelViewSet):
    queryset=Medicine.objects.all()
    serializer_class=MedicineSerializer

class LabTestViewSet(viewsets.ModelViewSet):
    queryset=LabTest.objects.all()
    serializer_class=LabTestSerializer

class ReceptionistViewSet(viewsets.ModelViewSet):
    queryset=Receptionist.objects.all()
    serializer_class=ReceptionistSerializer

class UserDetailsViewSet(viewsets.ModelViewSet):
    queryset=UserDetails.objects.all()
    serializer_class=UserDetailsSerializer

class PatientViewSet(viewsets.ModelViewSet):
    queryset=Patient.objects.all()
    serializer_class=PatientSerializer

class AppointmentViewSet(viewsets.ModelViewSet):
    queryset=Appointment.objects.all()
    serializer_class=AppointmentSerializer