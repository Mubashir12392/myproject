from django.shortcuts import render
from django.http import HttpResponse
from .models import Student

# Create your views here.

def index(request):
    hello = Student.objects.all()
    return HttpResponse(hello)