from django.contrib import admin

# Register your models here.

from app.models import *

admin.site.register(Employee)

admin.site.register(EmployeeDetails)

admin.site.register(Country)