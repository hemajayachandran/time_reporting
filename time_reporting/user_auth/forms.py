from django import forms
#from django.contrib.auth.models import User
from .models import Employee

passwordInputWidget = {
    'password': forms.PasswordInput(),
}

class SignUpForm(forms.ModelForm):
    #login = forms.EmailField(label='username', max_length=200, help_text="Enter your company email id")
    class Meta:
        model = Employee
        fields = '__all__'
        widgets = [passwordInputWidget]

class LoginForm(forms.ModelForm):
    login = forms.EmailField(label='Username', max_length=200, help_text="Enter your company email id")
    class Meta:
        model = Employee
        fields = ['login', 'password']
        widgets = [passwordInputWidget]
