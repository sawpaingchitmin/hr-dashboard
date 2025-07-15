from django.contrib import admin
from .models import Employee, Attendance

@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('name', 'department','role', 'salary', 'hire_date')
    search_fields = ('name', 'department', 'role', 'salary')

admin.site.register(Attendance)
