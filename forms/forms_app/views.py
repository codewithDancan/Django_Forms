from django.shortcuts import render
from django.http import HttpResponse
from .forms import EmployeeForm
from .models import Employee

# Create your views here.
def employee_data(request):
    if request.method == 'POST':
        form = EmployeeForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['emp_name']
            salary = form.cleaned_data['emp_salary']

            emp = Employee.objects.create(emp_name=name, emp_salary=salary)
            emp.save()
            return HttpResponse('Data has been saved successfully.')
    else:
        form = EmployeeForm()
    return render(request, 'employee.html', {'form': form})
