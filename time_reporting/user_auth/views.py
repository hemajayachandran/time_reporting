from django.shortcuts import render, redirect
from .forms import SignUpForm, LoginForm
from .models import Employee
from django.contrib.auth import authenticate
import logging

# Get an instance of a logger
logger = logging.getLogger(__name__)
logger_e = logging.getLogger('errors')

# Create your views here.

# Function will allow user to sign up
def signup(request):
    form = SignUpForm()
    success = None
    if request.method == 'POST':
        if Employee.objects.filter(login=request.POST['login']).exists():
            error = "This username is already taken"
            return render(request, 'registration/signup.html', {'form': form, 'error': error})
        form = SignUpForm(request.POST)
        new_user = form.save(commit=False)
        new_user.save()
        success = "New user account created successfully"
        return redirect('loginto')
    return render(request, 'registration/signup.html', {'form': form, 'success': success})

# This function allows user to login
def login(request):
    form = LoginForm()
    if 'user_id' in request.session:
        return redirect('timelog:index')
    error = None
    if request.method == 'POST':
        form = LoginForm(request.POST)
        username = request.POST['login']
        password = request.POST['password']
        if Employee.objects.filter(login=username, password=password).exists():
            user = Employee.objects.get(login=username, password=password)
            request.session['user_id'] = user.reference
            print(request.session)
            print(request.session['user_id'])
            return redirect('timelog:index')
        else:
            logger_e.error("User doesn't exist")
            error = "User doesn't exist"
    return render(request, 'registration/login.html', {'form': form, 'error': error})


def get_user(request):
    return Employee.objects.get(reference=request.session['user_id'])

# This allows user to logout from the session
def logout(request):
    if 'user_id' in request.session:
        del request.session['user_id']
    return redirect('loginto')
