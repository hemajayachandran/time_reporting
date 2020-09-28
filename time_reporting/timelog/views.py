from django.shortcuts import render, HttpResponse, redirect, get_object_or_404
from .forms import TimesheetForm
from user_auth.views import get_user
from user_auth.models import Employee
from .models import Hours
from time_reporting import settings
import logging
from django.views import View
from django.views.generic.list import ListView

# Get an instance of a logger
logger = logging.getLogger(__name__)
logger_e = logging.getLogger('errors')

# Create your views here.

def index(request, *args, **kwargs):
    data = Hours.objects.all()
    form = TimesheetForm(request.POST or None)
    context = {}
    context['reporting_year'], context['reporting_month'] = month_year(settings.REPORTING_DATE)
    if 'user_id' in request.session:
        user = get_user(request)
        context['user'] = user
        logger.info("Employee name:" + user.name)
    return render(request, 'timelog/index.html', {'form': form, 'data': data, 'context': context})

def create(request, *args, **kwargs):
    form = TimesheetForm(request.POST or None)
    context = {}
    context['reporting_year'], context['reporting_month'] = month_year(settings.REPORTING_DATE)
    context['m'] = request.GET.get('month')
    context['y'] = request.GET.get('year')
    data = Hours.objects.filter(month=request.GET.get('month'), year=request.GET.get('year'))
    if 'user_id' in request.session:
        user = get_user(request)
        context['user'] = user
        logger.info("Employee name:" + user.name)
    if form.is_valid():
        time = form.save(commit=False)
        time.reference_pk = Employee.objects.get(reference=request.session['user_id'])
        time.save()
        hours = Hours.objects.filter(reference_pk=request.session['user_id'], month=time.month, year=time.year).update(status="Submitted")
        success = "Timesheet submitted successfully"
        logger.info("Month: " + time.month + " " + "Year: " + time.year +
                    '\n' + "Week1: " + str(time.week1) + " " + "Week2: " + str(time.week2) + " " +
                    "Week3: " + str(time.week3) + " " + "Week4: " + str(time.week4) +
                    '\n' + "Total Hours: " + str(time.total_hours))
        logger.info("Timesheet submitted successfully")
        return redirect('timelog:index')
    return render(request, 'timelog/sheet.html', {'form': form, 'context': context, 'data': data})

def update(request, pk):
    hour = get_object_or_404(Hours, pk=pk)
    form = TimesheetForm(request.POST or None, instance=hour)
    context = {}
    context['pk'] = pk
    context['year'], context['month'] = hour.year, hour.month
    context['reporting_year'], context['reporting_month'] = month_year(settings.REPORTING_DATE)
    if 'user_id' in request.session:
        user = get_user(request)
        logger.info("Employee name:" + user.name)
    print("befiore")
    print(form.errors)
    if form.is_valid():
        print("Inside validation")
        obj = form.save(commit=False)
        obj.save()
        logger.info("Month: " + obj.month + " " + "Year: " + obj.year +
                    '\n' + "Week1: " + str(obj.week1) + " " + "Week2: " + str(obj.week2) + " " +
                    "Week3: " + str(obj.week3) + " " + "Week4: " + str(obj.week4) +
                    '\n' + "Total Hours: " + str(obj.total_hours))
        logger.info("Timesheet updated successfully")
        return redirect('timelog:index')
    return render(request, 'timelog/update.html', {'form': form, 'user': user, 'context': context} )


def month_year(reporting_date):
    year = reporting_date[:4]
    month = reporting_date[5:7]
    return year, month
