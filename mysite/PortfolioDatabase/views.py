from django.shortcuts import render
from django.http import HttpResponse
from .models import hobbies
from .models import portfolio
from django.template import loader

# Create your views here.
def Home(request):
    template = loader.get_template('PortfolioDatabase/Home.html')
    context = {}
    return HttpResponse(template.render(context, request))

def Hobbies(request):
    hobbie_list = hobbies.objects.all()
    template = loader.get_template('PortfolioDatabase/Hobby.html')
    context = {
        'hobbie_list': hobbie_list,
    }
    return render(request, 'PortfolioDatabase/Hobby.html', context)

def hobDetail(request, id):
    hobby = hobbies.objects.get(pk=id)
    context = {
        'hobby': hobby
    }
    return render(request,'PortfolioDatabase/HobDetail.html', context)

def Portfolio(request):
    port_list= portfolio.objects.all()
    template = loader.get_template('PortfolioDatabase/Portfolio.html')
    context ={
        'port_list': port_list
    }
    return render(request, 'PortfolioDatabase/Portfolio.html', context)
def PortDetail(request, id):
    port = portfolio.objects.get(pk=id)
    context = {
        'port': port
    }
    return render(request,'PortfolioDatabase/PortDetail.html', context)

def Contact(request):
    template = loader.get_template('PortfolioDatabase/Contact.html')
    context = {}
    return HttpResponse(template.render(context, request))