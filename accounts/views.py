from django.shortcuts import render, redirect
from django.contrib import messages, auth
from django.core.validators import validate_email
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .models import FormContact

def login(request):
    if request.method != 'POST':
        return render(request, 'accounts/index_login.html')
    username = request.POST.get('username')
    password = request.POST.get('password')
    user = auth.authenticate(request, username = username, password = password)
    
    if not user:
        messages.error(request,'Invalid Username or Password, please try again or register')
        return render(request, 'accounts/index_login.html')
    else:
        auth.login(request, user)
        messages.success(request,'Logged in')
        return redirect('dashboard')


def logout(request):
    auth.logout(request)
    return redirect('login')

def register(request):
    if request.method != 'POST':
        return render(request, 'accounts/register.html')
    name = request.POST.get('name')
    last_name = request.POST.get('last_name')
    email = request.POST.get('email')
    username = request.POST.get('username')
    password = request.POST.get('password')
    password_2 = request.POST.get('password_2')

    if not name or not last_name or not email or not username or not password or not password_2 :
        messages.error(request,'You must fill in all the register fields')
        return render(request, 'accounts/register.html')

    try:
        validate_email(email)
    except:
        messages.error(request,'Invalid E-mail')
        return render(request, 'accounts/register.html')

    if len(password) < 6:
        messages.error(request,'Password must contain a mininum of 6 characters')
        return render(request, 'accounts/register.html')

    if password != password_2:
        messages.error(request,'Confirm password must be valid')
        return render(request, 'accounts/register.html')

    if User.objects.filter(username = username).exists():
        messages.error(request,'Username already exists')
        return render(request, 'accounts/register.html')

    if User.objects.filter(email = email).exists():
        messages.error(request,'Email already exists')
        return render(request, 'accounts/register.html')
    
    messages.success(request,'Successfully registered')
    user = User.objects.create_user(username = username, email = email, password = password, first_name = name,
    last_name = last_name)
    user.save()
    return redirect('login')

@login_required(redirect_field_name='login')
def dashboard(request):
    if request.method != 'POST':
        form = FormContact
        return render(request, 'accounts/dashboard.html', {'form':form})

    form = FormContact(request.POST, request.FILES)

    if not form.is_valid():
        messages.error('Something goes wrong, please register the contact again')
        form = FormContact(request.POST)
        return render(request, 'accounts/dashboard.html', {'form':form})

    form.save()
    messages.success(request,f'Contact {request.POST.get("name")} {request.POST.get("last_name")} saved')
    return redirect('dashboard')
