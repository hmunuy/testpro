from django.shortcuts import render
from django.shortcuts import redirect
from django.views.generic import TemplateView
from django.template import loader
from django.contrib.auth.models import User,auth
from django.contrib import messages
from .models import Host
from .models import snmp_ap
from .models import snmp_data
import datetime
# from .models import snmpdata
import requests
from django.http import HttpResponse




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
    username = request.session['username']
    # data = list(Host.objects.all().distinct())
    # in_time = Host.objects.latest('insert_time')
    # data = Host.objects.all().filter(insert_time='in_time').order_by('-description')
    data = Host.objects.values('hostname','description','uptime','insert_time').distinct()
    # x = data.query
    if username != "" :
       return render(request,'home.html',{'data':data})
    else:
        return render(request,'registeradmin.html')
           
    
    # Check Login
    # username = request.GET['username']
    # password = request.GET['password']
    # if ((username == 'admin') and  (password == 'admin'))  :
    #     msg = ("เข้าสู่ระบบ โดย คุณ :"+username)
    #     r = requests.post(url, headers=headers , data = {'message':msg})
    


    
    # else:
    #     msg = ("มีการพยายามเข้าสู่ระบบ โดย คุณ :"+username)
    #     r = requests.post(url, headers=headers , data = {'message':msg})
    #     return render(request,'index.html')
def registeradmin(request):
    
    return render(request,'registeradmin.html')

def monitor(request):
    username = request.session['username']
    data = snmp_data.objects.values('ip_hostname','hostname','interface_snmp','status_snmp').distinct()
    # x_time = datetime.datetime.now()
    # x_time_sum = x_time.strftime('%d:'+'%A:'+'%B:'+'%Y:'+'%H:'+'%M')
    # data2 = snmp_ap.objects.all().filter(insert_time=x_time_sum).order_by('-numuser_wlc')
    data2 = snmp_ap.objects.all()
    for qry in data2 :
        sum_user = 0
        num = qry.numuser_wlc
        sum_user = sum_user + num
    x_sum = sum_user
        
    if username != "" :
       return render(request,'monitor.html',{'data':data,'data2':x_sum}) 
    else:
        return render(request,'registeradmin.html')
    return render(request, 'monitor.html', {"username" : username})
   
    # device = request.POST('device')
       
    # try:
    #     print(device)
    #     return render(request,'topology.html')
    # except NameError:
    #     print("Error")
    # else:
    #     return render(request,'home.html')
    
    # if request.method == 'POST' and 'device' in request.POST:
    #    device = request.POST['device']
    #    if device is not None and device !='':
    #       data = list(User.objects.filter(username=device).distinct())
    #       return render(request,'monitor.html',{'data':data})
    #    else:
    #         pass

def wlc_ap(request):
    username = request.session['username']
    butthon = request.POST['butthon']
    if butthon == 'butthon' :
        num_wlc = snmp_ap.objects.all().latest
       
        return render(request, 'monitor.html',{'num_wlc':num_wlc})
    else : return redirect('monitor.html')


def main1(request):
    if request.session.has_key('username'):
       username = request.session.GET['username']
       return render(request, 'main.html', {"username" : username})
    else:
       return render(request, 'index.html', {})
    return render(request,'home.html')


  

def topology(request):
    username = request.session['username']
    
    
    # if request.POST['search'] =='' :
    #     device = request.POST['search']
    #     return render(request,'/infodevice/',device)
    return render(request,'topology.html',{'username':username})

def infodevice(request,serach):
    username = request.session['username']
    device = serach
    return render(request,'infodevice.html',{'username':username})    

def topology_serach(request):
    username = request.session['username']
    serach = request.POST['serach']
    if serach :
    
        return redirect('/infodevice/',serach)
    infodevice(serach)

def register(request):
    username = request.session['username']
    data = list(User.objects.filter(username=username).distinct())
    
    return render(request,'register.html',{'data':data})

def report(request):
    data1 = list(Host.objects.all().distinct())
    return render(request,'report.html',{'data':data1})

def addUser(request):
    username = request.session['username']
    username1 = request.POST['username']
    firstname = request.POST['firstname']
    lastname = request.POST['lastname']
    email = request.POST['email']
    password = request.POST['password']
    repassword = request.POST['repassword']

    if password==repassword :
        if User.objects.filter(username=username1).exists():
            messages.info(request,'UserName นีมีคนใช้แล้ว')
            return redirect('/registeradmin/')
        elif User.objects.filter(email=email).exists():
            messages.info(request,'Email นี้เคยลงทะเบียนแล้ว')
            return redirect('/registeradmin/')
        else :
            user =  User.objects.create_user(
                username = username1,
                password = password,
                email = email,
                first_name = firstname,
                last_name = lastname
                )
            user.save()
            msg = ("คุณ : "+username1+" ถูกลงทะเบียนโดย : "+username+" เรียบร้อยกรุณาตรวจสอบ")
            r = requests.post(url, headers=headers , data = {'message':msg})
            messages.info(request,'ลงทะเบียนสำเร็จ')
            return redirect('/registeradmin/')  
    else  :
         messages.info(request,'รหัสผ่านไม่ตรงกัน')
         return redirect('/registeradmin/')   
    
        
       
        # return redirect('/registeradmin/')

def login(request):
    username = request.POST['username']
    password = request.POST['password']

    #check username ,password
    user=auth.authenticate(username=username,password=password)

    if user is not None :
       request.session.set_expiry(86400)
       auth.login(request,user)
       username = user.username
       request.session['username'] = username
       msg = ("เข้าระบบโดย :"+username)
       r = requests.post(url, headers=headers , data = {'message':msg})
       return redirect('home')
    else :
        messages.info(request,'ไม่พบข้อมูล')
        msg = ("พยายามเข้าระบบโดย :"+username)
        r = requests.post(url, headers=headers , data = {'message':msg})
        return redirect('/')
    

def logout(request):
    auth.logout(request)
    user_logout = request.session.get('username', None)
    current_expiry = request.session.get('username')
    if user_logout:
        request.session['username'] = user_logout
        if current_expiry:
           request.session['username'] = current_expiry
           msg = ("ออกจากระบบเเล้ว")
           r = requests.post(url, headers=headers , data = {'message':msg})
    return render(request,'index.html')





