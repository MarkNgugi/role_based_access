from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required
def dashboard(request):
    # Get user's group memberships
    context = {
        'is_admin': request.user.groups.filter(name="Admin").exists(),
        'is_hr_manager': request.user.groups.filter(name="HR Manager").exists(),
        'is_manager': request.user.groups.filter(name="Manager").exists(),
        'is_employee': request.user.groups.filter(name="Employee").exists(),
    }
    
    return render(request, 'main_app/dashboard.html', context)

@login_required
def admin_dashboard(request):
    return render(request, 'main_app/admin_dashboard.html')

@login_required
def hr_dashboard(request):
    return render(request, 'main_app/hr_dashboard.html')

@login_required
def manager_dashboard(request):
    return render(request, 'main_app/manager_dashboard.html')

@login_required
def employee_dashboard(request):
    return render(request, 'main_app/employee_dashboard.html')

