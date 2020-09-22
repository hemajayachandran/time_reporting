from django.db import models
#from django.db.models import CheckConstraint, Q

# Create your models here.

class Employee(models.Model):
    reference = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100, null=True, help_text="Enter your full name")
    login = models.CharField(max_length=200, help_text="Enter your company email id")
    password = models.CharField(max_length=20)

"""class Hours(models.Model):
    MONTHS = (
        ('01', 'JAN'),
        ('02', 'FEB'),
        ('03', 'MAR'),
        ('04', 'APR'),
        ('05', 'MAY'),
        ('06', 'JUN'),
        ('07', 'JUL'),
        ('08', 'AUG'),
        ('09', 'SEP'),
        ('10', 'OCT'),
        ('11', 'NOV'),
        ('12', 'DEC')
    )
    YEARS = (
        ("2015", "2015"),
        ("2016", "2016"),
        ("2018", "2018"),
        ("2019", "2019"),
        ("2020", "2020")
    )
    reference_pk = models.ForeignKey(Employee, on_delete=models.CASCADE)
    month = models.CharField(max_length=2, choices=MONTHS)
    year = models.CharField(max_length=4, choices=YEARS)
    submitting_date = models.DateTimeField(auto_now_add=True)
    total_hours = models.DecimalField(max_digits=5, decimal_places=2)
    week1 = models.DecimalField(max_digits=2, decimal_places=2)
    week2 = models.DecimalField(max_digits=2, decimal_places=2)
    week3 = models.DecimalField(max_digits=2, decimal_places=2)
    week4 = models.DecimalField(max_digits=2, decimal_places=2)

    class Meta:
        verbose_name_plural = "Hours"
        unique_together = [
            ("month", "year"),
        ]
        constraints = [
            CheckConstraint(check=Q(week1__lt=40.00), name="week1_hour_max"),
            CheckConstraint(check=Q(week2__lt=40.00), name="week2_hour_max"),
            CheckConstraint(check=Q(week3__lt=40.00), name="week3_hour_max"),
            CheckConstraint(check=Q(week4__lt=40.00), name="week4_hour_max"),

        ]"""
