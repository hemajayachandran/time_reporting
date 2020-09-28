from django.db import models
from user_auth.models import Employee



# Create your models here.
class Hours(models.Model):

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
        ('2015', "2015"),
        ('2016', "2016"),
        ('2018', "2018"),
        ('2019', "2019"),
        ('2020', "2020")
        )
    STATUS = (
        ('Pending', 'Pending'),
        ('Submitted', 'Submitted'),
        ('Completed', 'Completed')
    )

    reference_pk = models.ForeignKey(Employee, on_delete=models.CASCADE)
    month = models.CharField(max_length=2, choices=MONTHS, default='JAN')
    year = models.CharField(max_length=4, choices=YEARS, default='2020')
    submitting_date = models.DateTimeField(auto_now_add=True)
    total_hours = models.DecimalField(max_digits=5, decimal_places=2)
    week1 = models.DecimalField(max_digits=4, decimal_places=2)
    week2 = models.DecimalField(max_digits=4, decimal_places=2)
    week3 = models.DecimalField(max_digits=4, decimal_places=2)
    week4 = models.DecimalField(max_digits=4, decimal_places=2)
    status = models.CharField(max_length=20, choices=STATUS, default='Pending')


    class Meta:
        verbose_name_plural = "Hours"
        unique_together = [
            ("month", "year"),
        ]

    def __str__(self):
        return "%s" %(self.reference_pk)
