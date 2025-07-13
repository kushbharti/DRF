from django.urls import path,include
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'emp',views.EmployeeViewset)

urlpatterns = [
    # path('emp/',views.Employee.as_view()),
    # path('emp/<int:pk>',views.EmployeeDetail.as_view()),
    
    path('',include(router.urls))
    
]