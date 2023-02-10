from pickle import GET
from django.shortcuts import render,redirect
from .forms import EmployeeForm
from .models import Employee
from django.http import JsonResponse
from django.core import serializers
from .serializers import EmployeeSerializer
from rest_framework import status
from rest_framework.response import Response
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view



def employee_List(request):
    # context = {'employee_list':Employee.objects.all()}
    # return render(request, "employee_register/employee_list.html",context)
    context = Employee.objects.all()
    serializer = EmployeeSerializer(context,many=True)
    return JsonResponse(serializer.data, safe=False)

@csrf_exempt
@api_view(['POST','PUT'])
def employee_form(request,id=0):
    # if request.method == 'GET':
    #     if id == 0:
    #         form = EmployeeForm()
    #     else:
    #         employee = Employee.objects.get(pk=id)
    #         form = EmployeeForm(instance=employee)
    #     return render(request, "employee_register/employee_form.html",{'form':form})
    # else:
    #     if id ==0:
    #         form = EmployeeForm(request.POST)
    #     else:
    #         employee = Employee.objects.get(pk=id)
    #         form = EmployeeForm(request.POST,instance=employee)
    #     if form.is_valid():
    #         form.save()
    #     return redirect('/employee/list')

    if request.method == 'GET':
        context = Employee.objects.all()
        serializer = EmployeeSerializer(context,many=True)
        return JsonResponse(serializer.data, safe=False)

    if request.method == 'POST':
        # print(request.data)
        serializer = EmployeeSerializer(data=request.data)
        # print(serializer.is_valid())
        # print(serializer.errors)
        if serializer.is_valid():
            # print("hello")
            serializer.save()
            return Response(serializer.data,status = status.HTTP_201_CREATED)

    if request.method == 'PUT':
        try:
            context = Employee.objects.get(pk=id)
        except Employee.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        serializer = EmployeeSerializer(context, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_404_BAD_REQUEST)
            

    

    


@csrf_exempt
def employee_delete(request,id):
    employee = Employee.objects.get(pk=id)
    employee.delete()
    return redirect('/employee/list')