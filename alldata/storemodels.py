from django.db import models

# Create your models here.
class Employee(models.Model):
	Employee_Name=models.CharField(max_length=120,null=True)
	Unique_ID=models.CharField(max_length=70,null=True)
	Email_ID=models.CharField(max_length=120,null=True)
	Password=models.CharField(max_length=40,null=True)
	Joining_Date=models.DateField(max_length=120,null=True)


	def __str__(self):
		return str(self.Employee_Name)


	