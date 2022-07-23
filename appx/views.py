from datetime import datetime
from django.db.models import Q
from tokenize import group
from django.shortcuts import render
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
            my_type = "student"
            lname = Student.objects.filter(email=username)[0].first_name + " " + Student.objects.filter(email=username)[0].last_name
            today = datetime.today()

            context = {
            'type': my_type ,"name": lname , "today": today
            }

        if Teacher.objects.filter(email=username).filter(password=password):
            my_type = "teacher" 
            lname = Teacher.objects.filter(email=username)[0].first_name + " " + Teacher.objects.filter(email=username)[0].last_name
            studentlist = Student.objects.all()
            total_projects = Student.objects.all().filter(~Q(group_no=0))
            total = len(total_projects)
            project_progress = Student.objects.all().filter(~Q(project_progress=100))
            currrent = len(project_progress)
            today = datetime.today()

            context = {
            'type': my_type ,"name": lname , "studentlist": studentlist ,"total": total ,"current": currrent , "today": today
            }

        
        return render(request, "dashboard.html", context)
    else:
        return render(request, 'login.html')

def dashboard(request):
    return render(request, 'dashboard.html')