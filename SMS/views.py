from SMS.models import Courses, Students
import os
from django.http.response import Http404, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

# Create your views here.


def home(request):
    return render(request, "index.html")


def studenthome(request):
    return render(request, "student.html")


def adminhome(request):
    return render(request, "admin.html")


def add_course(request):
    return render(request, "add-course.html")


def addcourse(request):
    queryset = {}
    if request.method == 'POST':
        data = request.POST.copy()
        del data['csrfmiddlewaretoken']
        course_model = Courses(
            id=data['CourseId'], course_name=data['CourseName'], duration=data['CourseDur'], fees=data['Fees'])
        course_model.save()
        queryset['success'] = True
    return render(request, "add-course.html", queryset)


def viewcourse(request):
    CourseList = Courses.objects.all()
    return render(request, "view-course.html", {"CourseList": CourseList})


def search(request):
    context = {}
    if request.method == 'POST':
        data = request.POST.copy()
        del data['csrfmiddlewaretoken']
        flag = False
        value = data['StudentId']
        try:
            context['data'] = Students.objects.get(rollno=value)
        except Students.DoesNotExist:
            raise Http404
    return render(request, "view-student.html", context)


def register(request):
    queryset = {}
    if request.method == 'POST':
        data = request.POST.copy()
        del data['csrfmiddlewaretoken']
        student_model = Students(
            rollno=data['Studentid'], name=data['StudentName'], dob=data['DOB'], course_id=Courses.objects.get(id=data['Courseid']))
        student_model.save()
        queryset['success'] = True
    return render(request, "add-student.html", queryset)


def viewcoursestudent(request):
    CourseList = Courses.objects.all()
    return render(request, "view-course-student.html", {"CourseList": CourseList})


def applycourse(request):
    queryset = {}
    if request.method == 'POST':
        data = request.POST.copy()
        del data['csrfmiddlewaretoken']
        value = data['Studentid']
        try:
            context = Students.objects.get(rollno=value)
            student_model = Students(
                rollno=context.rollno, name=context.name, dob=context.dob, course_id=Courses.objects.get(id=data['Courseid']))
            student_model.save()
            queryset['success'] = True
        except Students.DoesNotExist:
            raise Http404
    return render(request, "apply-course.html", queryset)
