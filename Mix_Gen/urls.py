from django.urls import path,include
from .views import Emps,Emps_
urlpatterns = [
    # path('emp/',views.Employee.as_view()),
    # path('emp/<int:pk>',views.EmployeeDetail.as_view()),
    path('employee/',Emps.as_view()),
    path('employee/<int:pk>/',Emps_.as_view()),
    

]