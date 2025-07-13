from rest_framework.views import APIView
from .models import Employees
from .serializers import EmployeeSerializer
from rest_framework.response import Response
from rest_framework import status

# Create your views here.

class Employee(APIView):
    def get(self,request):
        employees = Employees.objects.all()
        serializer = EmployeeSerializer(employees ,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)
    
    def post(self,request):
        serializer = EmployeeSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.error,status=status.HTTP_400_BAD_REQUEST)
    
    
class EmployeeDetail(APIView):
    def get_object(self,pk):
        try:
            return Employees.objects.get(pk=pk)
        except Exception as e:
            return Response(status=status.HTTP_404_NOT_FOUND)
        
    def get(self,request,pk):
        emp = self.get_object(pk)
        serializer = EmployeeSerializer(emp)
        return Response(serializer.data,status=status.HTTP_200_OK)
    
    def put(self,request,pk):
        emp = self.get_object(pk)
        serializer = EmployeeSerializer(emp,data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_200_OK)
        return Response(serializer.error,status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self,request,pk):
        emp = self.get_object(pk)
        emp.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)