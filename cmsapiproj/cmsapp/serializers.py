from rest_framework import serializers
from .models import Department,Doctor,Prescription,Medicine,LabTest,Receptionist,UserDetails,Patient,Appointment
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password

class SignupSerializer(serializers.ModelSerializer):
        def create(self, validated_data):
            # hash the password before saving
            validated_data['password'] = make_password(validated_data.get('password'))
            user = super(SignupSerializer, self).create(validated_data)
            return user
        
        class Meta:
            model = User #specify the model to be serialized
            fields = ['username', 'password'] #specify the fields to be


class LoginSerializer(serializers.ModelSerializer):
    username = serializers.CharField(max_length=150, required=True)
    class Meta:
        model = User #specify the model to be serialized
        fields = ['username', 'password'] #specify the fields to be serialized



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

class PatientSerializer(serializers.ModelSerializer):
    class Meta:
        model=Patient
        fields='__all__'

class AppointmentSerializer(serializers.ModelSerializer):
    class Meta:
        model=Appointment
        fields='__all__'