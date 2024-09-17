from django.contrib import admin

# Register your models here.

from .models import Employee

class EmployeeAdmin(admin.ModelAdmin):
    list_display=['name','id','designation','address','phone_number','salary',]
    ordering=['id']

admin.site.register(Employee,EmployeeAdmin)

