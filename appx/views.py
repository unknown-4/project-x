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
            print("login worked")
            my_type = "student"
            lname = Student.objects.filter(email=username).first_name
            

        if Teacher.objects.filter(email=username).filter(password=password):
            print("login worked")
            my_type = "teacher" 
            lname = Teacher.objects.filter(email=username)[0].first_name
            studentlist = Student.objects.all()      

        context = {
            'type': my_type ,"name": lname , "studentlist": studentlist
        }
        print(context)
        return render(request, "dashboard.html", context)
    else:
        return render(request, 'login.html')

def dashboard(request):
    return render(request, 'dashboard.html')