from __future__ import unicode_literals
from django.db import models

class teachermodel(models.Model):
    teachername=models.CharField(max_length=50)
    surname=models.CharField(max_length=40)
    odetail=models.TextField(max_length=140)
    number=models.IntegerField(max_length=20)
    emailadress=models.EmailField(max_length=130)

class coursemodel(models.Model):
    coursename=models.CharField(max_length=50)
    coursecode=models.CharField(max_length=40)
    courseclass=models.CharField(max_length=20)
    date=models.TimeField()
    oneteacher=models.OneToOneField(teachermodel)
    enrolledstudent=models.ManyToManyField(studentmodel)

class studentmodel(models.Model):
    studentname=models.CharField(max_length=50)
    surname=models.CharField(max_length=40)
    emailadress=models.EmailField(max_length=140)
    enrolledcourses=models.ManyToManyField(coursemodel)
