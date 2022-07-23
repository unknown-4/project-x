from django.db import models

# Create your models here.

class Student(models.Model):
    first_name = models.CharField(max_length=100)
    middle_name = models.CharField(max_length=100, null=True, blank=True, default="")
    last_name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100, null=False, blank=False)
    password = models.CharField(max_length=50, null=False, blank=False)
    project_name = models.CharField(max_length=100,null=True, blank=True, default="")
    project_tags = models.CharField(max_length=100,null=True, blank=True, default="")
    project_desc = models.CharField(max_length=1000, null=True, blank=True, default="")

    def __str__(self):
        return self.first_name + " " + self.last_name

class Teacher(models.Model):
    first_name = models.CharField(max_length=100)
    middle_name = models.CharField(max_length=100, null=True, blank=True, default="")
    last_name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100,null=False, blank=False)
    password = models.CharField(max_length=50, null=False, blank=False)

    
    def __str__(self):
        return self.first_name + " " + self.last_name
