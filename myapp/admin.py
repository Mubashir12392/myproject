from django.contrib import admin
from .models import Student,Teacher,Cars

# Register your models here.

class Student_data(admin.ModelAdmin):
    list_display = ('student_name','age','gender')

class Teacher_data(admin.ModelAdmin):
    list_display = ('teacher_name','teacher_age','gender')

class Car_data(admin.ModelAdmin):
    list_display = ('car_name','car_colour','car_price')

admin.site.register(Student,Student_data)
admin.site.register(Teacher, Teacher_data)
admin.site.register(Cars, Car_data)