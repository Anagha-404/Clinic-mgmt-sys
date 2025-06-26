from rest_framework import serializers
from .models import Department
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password

class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model=Department
        fields='__all__'