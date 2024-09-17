
from django.urls import path,include 

from .views import HomeView,Employeedetail,CreateEmployee,EmployeeUpdateView,EmployeeDeleteView

urlpatterns = [
    path("",HomeView.as_view(),name="home"),
    path("detail/<int:pk> /",Employeedetail.as_view(),name="detail"),
    path("create/",CreateEmployee.as_view(),name="create"),
    path("update/<int:pk>/",EmployeeUpdateView.as_view(),name="update"),
    path("delete/<int:pk>/",EmployeeDeleteView.as_view(),name="delete"),
]