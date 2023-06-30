from django.db import models

# Create your models here.

class Department(models.Model):
    name = models.CharField(max_length=250)
    location = models.CharField(max_length=200)
    
    def __str__(self):
        return self.name

class Role(models.Model):
    name = models.CharField(max_length=200)
    
    def __str__(self):
        return self.name

class Employee(models.Model):
    fname = models.CharField(max_length=200)
    lname = models.CharField(max_length=200)
    dept = models.ForeignKey(Department, on_delete=models.CASCADE)
    salary = models.IntegerField(default=0)
    bonus = models.IntegerField(default=0)
    role = models.ForeignKey(Role, on_delete=models.CASCADE)
    phone = models.IntegerField(default=0)
    hire_date = models.DateField()

    def __str__(self):
        return "%s %s %s" %(self.fname, self.lname, self.phone)

