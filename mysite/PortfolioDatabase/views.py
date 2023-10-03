from django.shortcuts import render
from django.http import HttpResponse
from .models import hobbies
from .models import portfolio

# Create your views here.
def Home(request):
    return HttpResponse('<h1>Welcome</h1>'
                        '<p> Hello my name is Austin Allred, i am a senior in college studying Computer Science</p>')

def Hobbies(request):
    hobbie_list = hobbies.objects.all()
    return HttpResponse(hobbie_list)

def Portfolio(request):
    port_list= portfolio.objects.all()
    return HttpResponse(port_list)

def Contact(request):
    return HttpResponse('austinallred5@mail.weber.edu')