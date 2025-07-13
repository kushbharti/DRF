from django.urls import path
from . import views


#employee/v1/
urlpatterns =[
    path('employee/',views.Employee.as_view()),
    path('employee/<int:pk>',views.EmployeeDetail.as_view())
]