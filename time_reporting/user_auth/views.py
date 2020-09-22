from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate
from django.views.generic import TemplateView
from django.contrib.auth.views import LoginView
from .forms import LoginForm, SignUpForm
from .models import Employee

# Create your views here.
class HomeView(TemplateView):
    template_name = 'home.html'

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            name = form.cleaned_data.get('name')
            login = form.cleaned_data.get('login')
            password = form.cleaned_data.get('password')
            Employee.objects.create(name=name, login=login, password=password)
            return redirect('loginto')
    else:
        form = SignUpForm()
    return render(request, 'registration/signup.html', {'form': form})


class LoginPageView(LoginView):
    template_name = 'registration/login.html'
    authentication_form = LoginForm
