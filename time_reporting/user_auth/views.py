from django.shortcuts import render, redirect
from .forms import SignUpForm, LoginForm
from .models import Employee
from django.contrib.auth import authenticate


#from .models import Employee

# Create your views here.


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

def login(request):
    form = LoginForm()
    if 'user_id' in request.session:
        return redirect('timelog:index')
    #error = None
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
    return render(request, 'registration/login.html', {'form': form})

def get_user(request):
    return Employee.objects.get(reference=request.session['user_id'])

def home(request):
    if 'user_id' in request.session:
        user = get_user(request)
        return render(request, 'home.html', {'user': user})
    else:
        return redirect('loginto')

def logout(request):
    if 'user_id' in request.session:
        del request.session['user_id']
    return redirect('loginto')
