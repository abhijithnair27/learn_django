from dataclasses import field
from rest_framework import serializers
from .models import Employee

class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = ['firstname', 'lastname','emp_code','mobile','address','fathername','position']

