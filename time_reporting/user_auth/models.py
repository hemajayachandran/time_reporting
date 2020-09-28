from django.db import models

# Create your models here.
class Employee(models.Model):
    reference = models.AutoField(primary_key=True, unique=True)
    name = models.CharField(max_length=100, null=True, help_text="Enter your full name")
    login = models.EmailField(max_length=200, unique=True, help_text="Enter your company email id")
    password = models.CharField(max_length=20)


    def __str__(self):
        return self.name
