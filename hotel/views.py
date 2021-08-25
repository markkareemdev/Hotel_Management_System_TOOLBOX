
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from hotel.forms import UserRegisterForm, ReceptionistRegisterForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from django import forms
from .models import User, Receptionist,Room,RoomStatus,RoomType
# from django.contrib.auth.models import User
# from django.contrib.auth.forms import UserCreationForm


# from django.urls import reverse


def homepage(request):
    return render(request,'hotel/index.html')
    
def about(request):
    return render(request,'hotel/about.html')




# authorization and authentication    

def admin_create(request):
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, "Your account has been created successfully! You are now able to log in")
            return redirect('admin-login')
    else:
        form = UserRegisterForm()
    return render(request, 'hotel/register.html', {'form': form})

def register_receptionist(request):
    if request.method == "POST":
        form = ReceptionistRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            first_name = form.cleaned_data.get('first_name')
            messages.success(request, "Your account has been created successfully as a Receptionist! You are now able to log in")
            return redirect('admin-login')
    else:
        form = ReceptionistRegisterForm()
    return render(request, 'hotel/register_Reception.html', {'form': form})


@login_required
def profile(request):
    return render(request, 'hotel/profile.html')

@login_required
def dashboard(request):
    return render(request, 'hotel/dashboard.html', {'dash': 'This is the dashboard'})

def admin_list(request):
    hotel_admin_list = User.objects.all()
    return render(request, 'hotel/admin_list.html', {'admin_lists': hotel_admin_list})


def show_admin(request, uuid):
    display_admin = Receptionist.objects.get(uuid(uuid))
    return render(request, 'hotel/show_admin.html', {'show_admin': display_admin})

def edit_admin(request, id):
    pass

def delete_admin(request, id):
    pass

def logs(request):
    pass







