from email.policy import default
from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from multiselectfield import MultiSelectField
# Create your models here.


class Student(models.Model):
    first_name = models.CharField(max_length=100)
    middle_name = models.CharField(max_length=100, null=True, blank=True, default="")
    last_name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100, null=False, blank=False)
    password = models.CharField(max_length=50, null=False, blank=False)
    project_name = models.CharField(max_length=100,null=True, blank=True, default="")
    project_stage = models.CharField(max_length=100,null=True, blank=True, default="")
    project_desc = models.CharField(max_length=1000, null=True, blank=True, default="")
    project_link = models.URLField(max_length=100,null=True, blank=True, default="")
    project_sub_date = models.DateField(null=True, blank=True, default=None)
    project_progress = models.IntegerField(null=True, blank=True, default=0,validators=[MinValueValidator(0),
                                       MaxValueValidator(100)])
    group_no = models.IntegerField(null=True, blank=True, default=0,)


    def __str__(self):
        return self.first_name + " " + self.last_name

class Teacher(models.Model):
    first_name = models.CharField(max_length=100)
    middle_name = models.CharField(max_length=100, null=True, blank=True, default="")
    last_name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100,null=False, blank=False)
    password = models.CharField(max_length=50, null=False,)

    def __str__(self):
        return self.first_name + " " + self.last_name
    

class Time_line(models.Model):
    zero = models.DateField(null=True, blank=True, default=None)
    first = models.DateField(null=True, blank=True, default=None)
    second = models.DateField(null=True, blank=True, default=None)
    third = models.DateField(null=True, blank=True, default=None)
    fourth = models.DateField(null=True, blank=True, default=None)





