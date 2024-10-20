from django.db import models
from django.contrib.auth.models import Group, Permission

def create_groups():
    # Create groups
    admin_group, created = Group.objects.get_or_create(name='Admin')
    hr_manager_group, created = Group.objects.get_or_create(name='HR Manager')
    manager_group, created = Group.objects.get_or_create(name='Manager')
    employee_group, created = Group.objects.get_or_create(name='Employee')

    # Admins - all permissions 
    admin_permissions = Permission.objects.all()  # Get all permissions
    admin_group.permissions.set(admin_permissions)

    # HR Managers - limited permissions
    hr_manager_permissions = Permission.objects.filter(codename__in=[
        'view_employee', 'add_employee', 'change_employee', 'delete_employee',
        'view_leave', 'change_leave', 'view_performance',
    ])
    hr_manager_group.permissions.set(hr_manager_permissions)

    # Managers - view-only permissions
    manager_permissions = Permission.objects.filter(codename__in=[
        'view_employee', 'view_performance', 'change_leave'
    ])
    manager_group.permissions.set(manager_permissions)

    # Employees - self-service permissions
    employee_permissions = Permission.objects.filter(codename__in=[
        'view_self_data', 'change_self_data', 'apply_leave'
    ])
    employee_group.permissions.set(employee_permissions)

