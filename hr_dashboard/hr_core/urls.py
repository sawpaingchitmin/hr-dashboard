from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_redirect, name='home_redirect'),
    path('login/', views.custom_login, name='login'),
    path('logout/', views.custom_logout, name='logout'), 
    path('add/', views.add_employee, name="add_employee"),
    path('employees/', views.employee_list, name="employee_list"),
    path('employee/<int:pk>/', views.edit_employee, name='edit_employee'),
    path('attendance/', views.mark_attendance, name="mark_attendance"),
    path('employee-dashboard/', views.employee_dashboard, name="employee_dashboard"),
    path('attendance-history/', views.attendance_history, name="attendance_history"),
]