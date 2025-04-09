from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .forms import RegisterForm, LoginForm
from .models import Attendance
from django.contrib.auth.decorators import login_required
from django.contrib import messages

def register_view(request):
    form = RegisterForm(request.POST or None)
    if form.is_valid():
        user = form.save(commit=False)
        user.set_password(form.cleaned_data['password'])
        user.save()
        return redirect('login')
    return render(request, 'register.html', {'form': form})

def login_view(request):
    form = LoginForm(request, data=request.POST or None)
    if form.is_valid():
        user = form.get_user()
        login(request, user)
        return redirect('dashboard')
    return render(request, 'login.html', {'form': form})

@login_required
def dashboard_view(request):
    records = Attendance.objects.filter(user=request.user)
    return render(request, 'dashboard.html', {'records': records})

@login_required
def qr_scan_view(request):
    Attendance.objects.create(user=request.user)
    messages.success(request, "Attendance marked successfully!")
    return redirect('dashboard')

def logout_view(request):
    logout(request)
    return redirect('login')
