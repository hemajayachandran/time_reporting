from django import forms
from .models import Employee

class SignUpForm(forms.ModelForm):
    name = forms.CharField(max_length=100)
    login = forms.CharField(max_length=200)
    password = forms.CharField(max_length=20)

    class Meta:
        model = Employee
        fields = [
            'name',
            'login',
            'password'
        ]

class LoginForm(forms.ModelForm):
    login = forms.CharField(label="username", max_length=200)
    password = forms.CharField(max_length=20)

    class Meta:
        model = Employee
        fields = [
            'login',
            'password'
        ]
    def __init__(self, request, *args, **kwargs):
        super().__init__(*args, **kwargs)
