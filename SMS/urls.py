from django.contrib import admin
from django.urls import re_path, path
from .views import (
	home,
	studenthome,
	adminhome,
	addcourse,
	viewcourse,
	search,
	register,
	viewcoursestudent,
	applycourse,
	)

urlpatterns = [
	re_path(r'^$', home, name = 'home'),
	re_path(r'^Student$', studenthome, name = 'student'),
	re_path(r'^Admin$', adminhome, name = 'admin'),
	re_path(r'^add-course$', addcourse, name = 'addcourse'),
	re_path(r'^view-course$', viewcourse, name = 'viewcourse'),
	re_path(r'^view-student$', search, name = 'search'),
	re_path(r'^register-student$', register, name = 'register'),
	re_path(r'^view-course-student$', viewcoursestudent, name='viewcoursestudent'),
	re_path(r'^apply-course$', applycourse, name = 'applycourse'),
]
