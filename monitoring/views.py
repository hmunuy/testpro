from django.shortcuts import render
from django.views.generic import TemplateView
from django.template import loader
from .models import Host
import requests



# Create your views here.
url = 'https://notify-api.line.me/api/notify'
token = 'NuuUuOmWepLTjLylkfdFwppgMhxjTeNiF4wE6Kdg70a'
headers = {'content-type':'application/x-www-form-urlencoded','Authorization':'Bearer '+token}

#Query Data Host_snmp show in table on home.html page
# def hello(request):
#     data11 = "hnubyy"
#     return render(request,'home.html',{'hostname':data11})

def index(request):
    return render(request,'index.html')

def home(request):
    #Qury Data Show on Table in home.html
    data = list(Host.objects.all().distinct())
    # Check Login
    # username = request.GET['username']
    # password = request.GET['password']
    # if ((username == 'admin') and  (password == 'admin'))  :
    #     msg = ("เข้าสู่ระบบ โดย คุณ :"+username)
    #     r = requests.post(url, headers=headers , data = {'message':msg})
      

    return render(request,'home.html',{'data':data})

    
    # else:
    #     msg = ("มีการพยายามเข้าสู่ระบบ โดย คุณ :"+username)
    #     r = requests.post(url, headers=headers , data = {'message':msg})
    #     return render(request,'index.html')

def page2(request):
    return render(request,'page2.html')

def page3(request):
    return render(request,'page3.html')

def report(request):
    return render(request,'report.html')

# def login(request):
#     username = request.GET['username']
#     password = request.GET['password']
#     if ((username == 'admin') and  (password == 'admin'))  :
#         msg = ("เข้าสู่ระบบ โดย คุณ :"+username)
#         r = requests.post(url, headers=headers , data = {'message':msg})
      

#         return render(request,'home.html',{'username':username})
    
#     else:
#         msg = ("มีการพยายามเข้าสู่ระบบ โดย คุณ :"+username)
#         r = requests.post(url, headers=headers , data = {'message':msg})

#        return render(request,'index.html',{'username':username})
        
    

def logout(request):
    msg = ("ออกจากระบบเเล้ว")
    r = requests.post(url, headers=headers , data = {'message':msg})

    return render(request,'index.html')


