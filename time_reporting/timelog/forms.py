from django import forms
from .models import Hours
from time_reporting.settings import MAX_HOURS
import logging

logger_e = logging.getLogger('errors')

class TimesheetForm(forms.ModelForm):

    month = forms.ChoiceField(choices=Hours.MONTHS)
    class Meta:
        model = Hours
        fields = [
            'month',
            'year',
            'total_hours',
            'week1',
            'week2',
            'week3',
            'week4'
        ]

    def clean_week1(self):
        week1 = self.cleaned_data['week1']
        if week1 > MAX_HOURS:
            logger_e.error("Total hours for week1 exceeded it's limit")
            raise forms.ValidationError("Total hours for week1 exceeded it's limit")
        return week1

    def clean_week2(self):
        week2 = self.cleaned_data['week2']
        if week2 > MAX_HOURS:
            logger_e.error("Total hours for week2 exceeded it's limit")
            raise forms.ValidationError("Total hours for week2 exceeded it's limit")
        return week2

    def clean_week3(self):
        week3 = self.cleaned_data['week3']
        if week3 > MAX_HOURS:
            logger_e.error("Total hours for week3 exceeded it's limit")
            raise forms.ValidationError("Total hours for week3 exceeded it's limit")
        return week3

    def clean_week4(self):
        week4 = self.cleaned_data['week4']
        if week4 > MAX_HOURS:
            logger_e.error("Total hours for week4 exceeded it's limit")
            raise forms.ValidationError("Total hours for week4 exceeded it's limit")
        return week4
