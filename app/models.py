from django.db import models

# Create your models here.


class Employee(models.Model):
    EmployeeID=models.CharField(max_length=100,primary_key=True)
    FirstName= models.CharField(max_length=100)
    LastName=models.CharField(max_length=100)
    DepartmentNo=models.CharField(max_length=100)

class EmployeeDetails(models.Model):
    DepartmentNo=models.OneToOneField(Employee,on_delete=models.CASCADE)
    Address=models.TextField()
    PhoneNo=models.IntegerField()
    Email_Name=models.EmailField(max_length=200)

class Country(models.Model):
    Country_ID=models.IntegerField(primary_key=True)
    Country_Name=models.CharField(max_length=100)
