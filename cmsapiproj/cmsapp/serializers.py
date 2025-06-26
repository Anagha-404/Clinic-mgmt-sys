from rest_framework import serializers,Doctor,Prescription,Medicine,LabTest,Receptionist,UserDetails,RoleDetails,Patient,Appointment,Time
from .models import Department
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password

class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model=Department
        fields='__all__'

class DoctorSerializer(serializers.ModelSerializer):
    class Meta:
        model=Doctor
        fields='__all__'

class PrescriptionSerializer(serializers.ModelSerializer):
    class Meta:
        model=Prescription
        fields='__all__'

class MedicineSerializer(serializers.ModelSerializer):
    class Meta:
        model=Medicine
        fields='__all__'

class LabTestSerializer(serializers.ModelSerializer):
    class Meta:
        model=LabTest
        fields='__all__'

class ReceptionistSerializer(serializers.ModelSerializer):
    class Meta:
        model=Receptionist
        fields='__all__'

class UserDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model=UserDetails
        fields='__all__'

class RoleDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model=RoleDetails
        fields='__all__'

class PatientSerializer(serializers.ModelSerializer):
    class Meta:
        model=Patient
        fields='__all__'

class AppointmentSerializer(serializers.ModelSerializer):
    class Meta:
        model=Appointment
        fields='__all__'

class TimeSerializer(serializers.ModelSerializer):
    class Meta:
        model=Time
        fields='__all__'