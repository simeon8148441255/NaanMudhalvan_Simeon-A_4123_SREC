from django.shortcuts import render, redirect
from django.http import HttpResponse 


# Create your views here.
def display(request):
    return HttpResponse("welcome all")

def basic(request):
    return render(request,'basic.html')

def songpage2(request):
   return render(request, 'songpage2.html')

def songpage(request):
   return render(request, 'songpage.html')

def songpage3(request):
   return render(request, 'songpage3.html')

def Login(request):
   return render(request, 'Login.html')

def signup(request):
   return render(request, 'signup.html')