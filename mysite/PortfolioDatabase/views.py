from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import hobbies
from .models import portfolio
from django.template import loader
from .Forms import contactForms
from .Forms import portForms


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


def Create_contact(request):
    form = contactForms(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect("{% url 'Contact' %}")

    return render(request, 'PortfolioDatabase/Create_contact.html', {'form': form})

def Create_port(request):
    form = portForms(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('PortfolioDatabase:Portfolio')

    return render(request, 'PortfolioDatabase/Create_port.html', {'form':form})

def Update_port(request, id):
    port = portfolio.objects.get(id=id)
    form = portForms(request.POST or None, instance=port)

    if form.is_valid():
        form.save()
        return redirect('PortfolioDatabase:Portfolio')

    return render(request, 'PortfolioDatabase/Create_port.html', {'form':form, 'port':port})

def Delete_port(request, id):
    port = portfolio.objects.get(id=id)

    if request.method == 'POST':
        port.delete()
        return redirect('PortfolioDatabase:Portfolio')

    return render(request, 'PortfolioDatabase/Port-delete.html', {'port': port})