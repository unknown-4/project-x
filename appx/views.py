from datetime import datetime
from django.db.models import Q
from tokenize import group
from django.shortcuts import render
from . models import Student, Teacher , Time_line

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
            studentdetail = Student.objects.all().filter(email=username).filter(password=password)
            group_id = studentdetail[0].group_no
            group_name =  str(studentdetail[0].project_name)
            group_stage =  str(studentdetail[0].project_stage)
            group_desc =  str(studentdetail[0].project_desc)
            group_sub_date =  str(studentdetail[0].project_sub_date)
            group_progress =  str(studentdetail[0].project_progress)
            group_link  =   str(studentdetail[0].project_link)
            time_line = Time_line.objects.all()
            zero = time_line[0].zero
            first = time_line[0].first
            second = time_line[0].second
            third = time_line[0].third
            fourth = time_line[0].fourth
            print(zero)
            

            context = {
            'type': my_type ,"name": lname , "today": today , "group_id": group_id , "group_name": group_name , "group_stage": group_stage ,
             "group_desc": group_desc , "group_sub_date": group_sub_date , "group_progress": group_progress , "group_link" : group_link , 
                "zero": zero , "first": first , "second": second , "third": third , "fourth": fourth
            }

        elif Teacher.objects.filter(email=username).filter(password=password):
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
        else:
            context = {
            'type': my_type ,"name": "not logged in"
            }
            return render(request, "loginfailed.html", context)

        return render(request, "dashboard.html", context)
    else:
        return render(request, 'login.html')

def dashboard(request):
    return render(request, 'dashboard.html')

def loginfailed(request):
    return render(request,'loginfailed.html')

def verify(request, email):
    if request.method == 'GET':

        emailid = email
        studentdetail = Student.objects.all().filter(email=emailid)
        group_id = studentdetail[0].group_no
        group_name =  str(studentdetail[0].project_name)
        group_stage =  str(studentdetail[0].project_stage)
        group_desc =  str(studentdetail[0].project_desc)
        group_sub_date =  str(studentdetail[0].project_sub_date)
        group_progress =  str(studentdetail[0].project_progress)
        group_link  =   str(studentdetail[0].project_link)

        context = {
            'branch': email, "studentdetail": studentdetail , "group_id": group_id , "group_name": group_name , "group_stage": group_stage ,
                "group_desc": group_desc , "group_sub_date": group_sub_date , "group_progress": group_progress , "group_link" : group_link
        }   

        response = render(request, 'verify.html', context=context)
        return response
    else:
        response = render(request, 'verify.html', context=context)
        return response