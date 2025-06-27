from django.contrib.auth import authenticate
from django.shortcuts import render
from .models import Department,Doctor,Prescription,Medicine,LabTest,Receptionist,UserDetails,Patient,Appointment
from .serializers import DepartmentSerializer,DoctorSerializer,PrescriptionSerializer,MedicineSerializer, LabTestSerializer,ReceptionistSerializer, UserDetailsSerializer,PatientSerializer,AppointmentSerializer,SignupSerializer,LoginSerializer
from rest_framework import viewsets, status
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.authtoken.models import Token

# Create your views here.

class SignupAPIView(APIView):
    # allow any user to access this view
    permission_classes = [AllowAny]  # No authentication required for this view
    #override the post method to handle the signup request
    def post(self, request):
        serializer=SignupSerializer(data=request.data)
        if  serializer.is_valid():
            user = serializer.save()
            token, created = Token.objects.get_or_create(user=user)
            return  Response({
                'user_id': user.id,
                'username':  user.username,
                'token': token.key
            }, status=status.HTTP_201_CREATED)
        else:
            res = {'status': status.HTTP_400_BAD_REQUEST, 'data': serializer.errors}
            return Response(res, status=status.HTTP_400_BAD_REQUEST)


class LoginAPIView(APIView):
    # allow any user to access this view
    permission_classes = [AllowAny]  # No authentication required for this view
    #override the post method to handle the signup request
    def post(self, request):
        serializer=LoginSerializer(data=request.data)
        if  serializer.is_valid():
            #get username and password from the request data and authenticate the user
            username = serializer.validated_data.get('username')
            password = serializer.validated_data.get('password')
            #authenticate the user

            user = authenticate(request, username=username, password=password)
            if user is not None:
                token, created = Token.objects.get_or_create(user=user)
                response={'status':status.HTTP_200_OK,
                          'message': 'Login successful',
                          'username': user.username,
                          'data': {
                              'token': token.key}
                  }
                return Response(response, status=status.HTTP_200_OK)
            else:
                response={'status':status.HTTP_401_UNAUTHORIZED,
                          'message': 'Login NOT successful'}
                return Response(response, status=status.HTTP_401_UNAUTHORIZED)  # fixed: return immediately

        

        #if the serializer is not valid, return the errors
        response = {'status': status.HTTP_400_BAD_REQUEST,
                     'data': serializer.errors,
                    'message': 'Login NOT successful'}
        return Response(response, status=status.HTTP_400_BAD_REQUEST)

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