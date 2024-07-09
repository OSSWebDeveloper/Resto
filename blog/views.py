from django.shortcuts import render
from django.shortcuts import render, redirect, reverse

from django.utils import timezone
from .models import *
import random
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse

# Create your views here.
def index(request):

    menus = Menu.objects.all()[:9]
    obed = Obed.objects.all()[:9]
    ujin = Ujin.objects.all()[:9]
    povar = Povar.objects.all()[:4]
    return render(request, 'blog/index.html', {'posts' : menus, 'obets': obed , 'ujins':ujin , 'povars':povar})  
def about(request):
    posts = img.objects.all()
    povar = Povar.objects.all()[:4]

    return render (request, 'blog/about.html', {'posts':posts , 'povars':povar}) 

def contact(request):
    posts = img.objects.all()
    return render (request, 'blog/contact.html', {'posts':posts}) 

def booking(request):
    posts = img.objects.all()
    return render (request, 'blog/booking.html', {'posts':posts}) 

def  menu(request):
    menus = Menu.objects.all()[:9]
    obed = Obed.objects.all()[:9]
    ujin = Ujin.objects.all()[:9]
    povar = Povar.objects.all()[:4]
    return render (request, 'blog/menu.html', {'posts' : menus, 'obets': obed , 'ujins':ujin , 'povars':povar}) 


def service(request):
    posts = img.objects.all()
    return render (request, 'blog/service.html', {'posts':posts}) 

def team(request):
    povar = Povar.objects.all()
    return render (request, 'blog/team.html', {'povars':povar}) 

def testimonial(request):
    posts = img.objects.all()
    return render (request, 'blog/testimonial.html', {'posts':posts}) 

def base(request):
    posts = img.objects.all()
    return render (request, 'blog/base.html', {'posts':posts}) 

def Pages(request):
    posts = img.objects.all()
    return render (request, 'blog/Pages.html', {'posts':posts}) 





 

   

