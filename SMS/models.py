from django.db import models

# Create your models here.

class Courses(models.Model):
    id= models.AutoField(primary_key=True)
    course_name=models.CharField(max_length=255)
    duration = models.TextField()
    fees = models.IntegerField()


    def __str__(self):
        return self.course_name

    class Meta:
        app_label = 'SMS'


class Students(models.Model):
    rollno = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    dob=models.DateField()
    course_id=models.ForeignKey(Courses,on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.name

    class Meta:
        app_label = 'SMS'

