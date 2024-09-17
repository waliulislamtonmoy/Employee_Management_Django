from django.shortcuts import render


# Create your views here.
from .models import Employee

from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin


class HomeView(ListView):
    model=Employee
    template_name="App_Employee/Home.html"
    context_object_name='employee'
    ordering=["-id"]
    
class Employeedetail(DetailView):
    model=Employee
    template_name='App_Employee/DetailEmployee.html'
    

class CreateEmployee(LoginRequiredMixin,CreateView):
    model=Employee
    fields = ['name', 'address', 'phone_number', 'salary', 'designation', 'description']
    template_name="App_Employee/AddEmployee.html"
    success_url='/'



class EmployeeUpdateView(LoginRequiredMixin,UpdateView):
    model=Employee 
    fields = ['name', 'address', 'phone_number', 'description']
    template_name="App_Employee/AddEmployee.html"
    success_url="/"
    

class EmployeeDeleteView(LoginRequiredMixin,DeleteView):
    model=Employee 
    template_name="App_Employee/EmployeeDelete.html"
    success_url="/"