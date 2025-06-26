from django.shortcuts import render
from .models import Department
from .serializers import DepartmentSerializer
from rest_framework import viewsets

# Create your views here.

class DepartmentViewSet(viewsets.ModelViewSet):
    queryset=Department.objects.all()
    serializer_class=DepartmentSerializer