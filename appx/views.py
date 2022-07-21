import email
from django.contrib import messages
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from . models import Student, Teacher

# Create your views here.
def index(request):
    return render(request, 'index.html')

def login_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        
        my_type = "not_logged_in"

        if Student.objects.filter(email=username).filter(password=password):
            print("login worked")
            my_type = "student"

        if Teacher.objects.filter(email=username).filter(password=password):
            print("login worked")
            my_type = "teacher"

        context = {
            'type': my_type
        }
        print(context)
        return render(request, "dashboard.html", context)
    else:
        return render(request, 'login.html')

def logout_user(request):
    auth.logout(request)
    return redirect('index')

def dashboard(request):
    return render(request, 'dashboard.html')