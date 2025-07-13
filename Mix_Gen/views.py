from .serializers import EmployeesSerializer
from .models import Employees
from rest_framework import mixins
from rest_framework.generics import ListCreateAPIView,RetrieveUpdateDestroyAPIView
from rest_framework.throttling import ScopedRateThrottle

# Create your views here.

# Mixins

"""
class Employee(mixins.ListModelMixin,mixins.CreateModelMixin,generics.GenericAPIView):
    queryset = Employees.objects.all()
    serializer_class = EmployeesSerializer
    
    def get(self,request):
        return self.list(request)
    
    def post(self,request):
        return self.create(request)
    
    
class EmployeeDetail(mixins.RetrieveModelMixin,mixins.UpdateModelMixin,mixins.DestroyModelMixin,generics.GenericAPIView):
    queryset = Employees.objects.all()
    serializer_class = EmployeesSerializer
    
    def get(self, request, pk):
        return self.retrieve(request,pk)
    
    def put(self,request,pk):
        return self.update(request,pk)
    
    def delete(self,request,pk):
        return self.destroy(request,pk)
       
"""

# Generics

class Emps(ListCreateAPIView):
    queryset = Employees.objects.all()
    serializer_class = EmployeesSerializer
    throttle_classes = [ScopedRateThrottle]
    throttle_scope = 'emps'
    
class Emps_(RetrieveUpdateDestroyAPIView):
    queryset = Employees.objects.all()
    serializer_class = EmployeesSerializer
    throttle_classes =[ScopedRateThrottle]
    throttle_scope = 'emps_'