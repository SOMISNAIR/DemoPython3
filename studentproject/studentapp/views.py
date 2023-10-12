from django.http import HttpResponse
from django.shortcuts import render

from.models import Place
from .models import Person
# Create your views here.

def demo(request):
    obj=Place.objects.all()
    obj2=Person.objects.all()
    return render(request,"index.html",{'result':obj,'member':obj2})





# def display(request):
#     return HttpResponse("<h1>Hello world</h1>")
#
#
# def home(request):
#     return HttpResponse("<h1>HOME PAGE</h1>")
# def about(request):
#     return HttpResponse("<h1>I Am ABOUT</h1>")
# def contact(request):
#     return HttpResponse("<h1>I am CONTACT</h1>")
# def detail(request):
#     return render(request,"detail.html")
# def thanks(request):
#     return render(request,"thanks.html")
#
#
