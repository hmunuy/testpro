from django.shortcuts import render
# Create your views here.

def index(request):
    return render(request,'index.html')

def home(request):
    return render(request,'home.html')

def page2(request):
    return render(request,'page2.html')

def page3(request):
    return render(request,'page3.html')

def report(request):
    return render(request,'report.html')