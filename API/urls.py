from django.urls import path
from . import views

urlpatterns = [
    path('students/',views.studentview),
    path('students/<int:pk>',views.studentDetailview),
]