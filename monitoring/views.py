from django.shortcuts import render
from django.shortcuts import redirect
from django.views.generic import TemplateView
from django.template import loader
from django.contrib.auth.models import User,auth
from django.contrib import messages
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

def registeradmin(request):
    
    return render(request,'registeradmin.html')


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

def page4(request):
    return render(request,'page4.html')

def register(request):
    return render(request,'register.html')

def report(request):
    data1 = list(Host.objects.all().distinct())
    return render(request,'report.html',{'data':data1})

def addUser(request):
    username = request.POST['username']
    firstname = request.POST['firstname']
    lastname = request.POST['lastname']
    email = request.POST['email']
    password = request.POST['password']
    repassword = request.POST['repassword']

    if password==repassword :
        if User.objects.filter(username=username).exists():
            messages.info(request,'UserName นีมีคนใช้แล้ว')
            return redirect('/registeradmin')
        elif User.objects.filter(email=email).exists():
            messages.info(request,'Email นี้เคยลงทะเบียนแล้ว')
            return redirect('/registeradmin')
    elif password!=repassword :
         messages.info(request,'รหัสผ่านไม่ตรงกัน')
         return redirect('/registeradmin')
        
    else :
        user =  User.objects.create_user(
            username = username,
            password = password,
            email = email,
            first_name = firstname,
            last_name = lastname
            )
        user.save()
        return render(request,'registeradmin.html')

def login(request):
    username = request.POST['username']
    password = request.POST['password']

    #check username ,password
    user=auth.authenticate(username=username,password=password)

    if user is not None :
       auth.login(request,user)
       return redirect('/home/')
    else :
        messages.info(request,'ไม่พบข้อมูล')
        msg = ("พยายามเข้าระบบ")
        r = requests.post(url, headers=headers , data = {'message':msg})
        return redirect('/')
    

def logout(request):
    msg = ("ออกจากระบบเเล้ว")
    r = requests.post(url, headers=headers , data = {'message':msg})

    return render(request,'index.html')





