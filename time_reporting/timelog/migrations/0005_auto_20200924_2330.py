# Generated by Django 2.1.5 on 2020-09-24 23:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('timelog', '0004_hours_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hours',
            name='status',
            field=models.CharField(choices=[('Pending', 'Pending'), ('Submitted', 'Submitted'), ('Completed', 'Completed')], default='YET TO SUBMIT', max_length=20),
        ),
    ]
