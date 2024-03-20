from django.db import models

class Student(models.Model):

    CHOICES = (('male','Male'),
               ('female','Female'))

    student_name = models.CharField(max_length=50)
    age = models.IntegerField(default=0)
    gender = models.CharField(max_length=20, choices=CHOICES)


    

class Teacher(models.Model):

    CHOICES = (('male','Male'),
               ('female','Female'))

    teacher_name = models.CharField(max_length=50)
    teacher_age = models.IntegerField(default=0)
    gender = models.CharField(max_length=50, choices= CHOICES)



class Cars(models.Model):
    CHOICES = (('red', 'Red'),
               ('yellow','Yellow'),
               ('blue','Blue'),
               ('black','Black'))
    

    car_name = models.CharField(max_length=50)
    car_colour = models.CharField(max_length=20, choices= CHOICES)
    car_price = models.IntegerField(default=0)


