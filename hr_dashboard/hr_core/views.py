from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import Employee, Attendance
from django.contrib.auth import authenticate, login, logout 
from django.contrib import messages
from datetime import date
from django.utils import timezone
from django.db import IntegrityError

@login_required
def home_redirect(request):
    if request.user.is_superuser:
        return render(request, 'hr_core/dashboard.html', {'admin_name':request.user.get_full_name() or request.user.username})
    else:
        return redirect('employee_dashboard')  
    
def custom_login(request):
    if request.method == 'POST':
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None: 
            login(request, user) 
            if user.is_superuser:
                return redirect('home_redirect')
            else:
                return redirect('employee_dashboard') 
        else: 
            messages.error(request, "Invalid username or password")
    return render(request, "hr_core/login.html")

@login_required
def custom_logout(request): 
    logout(request)
    return redirect('login')

@login_required
def add_employee(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        if User.objects.filter(username=username).exists():
            messages.error(request, f"Username '{username}' is already taken. Please choose another username.")
            return render(request, "hr_core/add_employee.html", {"form_data": request.POST})

        user = User.objects.create_user(username=username, password=password)
       
        Employee.objects.create(
            user=user,
            name=request.POST.get("name"),
            department=request.POST.get("department"),
            role=request.POST.get("role"),
            salary=request.POST.get("salary"),
            email=request.POST.get("email"),
            phone_number=request.POST.get("phone_number"),
            address=request.POST.get("address"),
            hire_date=request.POST.get("hire_date"),
        )
        return redirect("employee_list")
       
    return render(request, 'hr_core/add_employee.html')

@login_required
def edit_employee(request, pk):
    employee = get_object_or_404(Employee, pk=pk)

    if request.method == "POST":
        if 'update' in request.POST:
            employee.name = request.POST.get('name')
            employee.department = request.POST.get('department')
            employee.role = request.POST.get('role')
            employee.salary = request.POST.get('salary')
            employee.email = request.POST.get('email')
            employee.phone_number = request.POST.get('phone_number')
            employee.address = request.POST.get('address')
            employee.hire_date = request.POST.get('hire_date')
            employee.save() 
            return redirect('employee_list')
        
        elif 'delete' in request.POST:
            employee.delete() 
            return redirect('employee_list')
    
    return render(request, 'hr_core/edit_employee.html', {'employee': employee})

@login_required
def employee_list(request):
    employees = Employee.objects.all()
    return render(request, 'hr_core/employee_list.html', {'employees': employees})


@login_required
def mark_attendance(request):
    if request.method == "POST":
        employee = request.user.employee
        today = date.today() 
        attendance, _ = Attendance.objects.get_or_create(employee=employee, date=today) 

        if 'check_in' in request.POST and not attendance.check_in:
            attendance.check_in = timezone.localtime().time()
        elif 'check_out' in request.POST and not attendance.check_out:
            attendance.check_out = timezone.localtime().time() 
        
        attendance.save()

    return redirect('employee_dashboard')

@login_required
def attendance_history(request):
    if request.user.is_superuser:
        records = Attendance.objects.select_related('employee').order_by('-date')
    else:
        records = Attendance.objects.filter(employee=request.user.employee).order_by('-date')
    
    return render(request, 'hr_core/attendance_history.html', {'records': records})

@login_required
def employee_dashboard(request):
    try:
        employee = request.user.employee
    except Employee.DoesNotExist:
        messages.error(request, "⚠️ Your employee account is no longer active or has been deleted. Please contact admin.")
        return redirect("login")
    
    today = date.today()
    attendance, _ = Attendance.objects.get_or_create(employee=employee, date=today)

    return render(request, "hr_core/employee_dashboard.html", {
        "employee": employee,
        "attendance": attendance
    })



