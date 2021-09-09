from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.views.decorators.csrf import csrf_protect
from pyexpat.errors import messages
from django.contrib.auth import authenticate, login
from Bookticket.models import Customer
from collections import OrderedDict
from datetime import datetime
import itertools


from .models import Customer,Routes, Trains, Schedule, Time
from django.contrib.auth.hashers import make_password, check_password
# Create your views here.


# def home(request):
#   return render(request, 'index.html', {})


from django.shortcuts import render
from django.views.generic.base import TemplateView


# Create your views here.



def home(request):
    return render(request, 'index.html')


def booktick(request):

    source="Goa"
    destination="Karnataka"
    Route_id=1
    slist=[]
    dlist=[]
    sql = 'select * from "Bookticket_routes"'
    print(sql)
    for p in Routes.objects.raw(sql):
        if p.source:
            slist.append(p.source)
        if p.destination:
            dlist.append(p.destination)
    sourcelist = list(OrderedDict.fromkeys(slist))
    destlist = list(OrderedDict.fromkeys(dlist))


    print(sourcelist)
    print("destinations")
    print(destlist)
    today=datetime.today().strftime('%Y-%m-%d')
    return render(request, 'bookticket.html',{'sourcelist':sourcelist,'destlist':destlist,'today':today})





from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib import auth
valueuser=""

def signup(request):
    if request.method == 'POST':
        if request.POST.get('name') and request.POST.get('email') and request.POST.get('age') and request.POST.get('phone') and request.POST.get('password'):
            post = Customer()
            post.Name = request.POST.get('name')
            post.Email = request.POST.get('email')
            post.Age = request.POST.get('age')
            post.Phone = request.POST.get('phone')
            post.Password = make_password(request.POST.get('password'))
            post.save()
            return redirect('/login')
        else:
            return render(request, 'register.html')
    else:
        return render(request, 'register.html')


from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm

from django.db import connection



def logout(request):
    # Log out the user.
    logout(request)
    # Return to homepage.
    return render(request, 'home.html')

@login_required(login_url='/login/')
@csrf_protect
def login(request):
    if request.method == 'POST':
        if request.POST.get('email') and request.POST.get('password'):
            email = request.POST.get('email')
            password = request.POST.get('password')
            y = []
            x = Customer.objects.get(Email=email)
            y.append(x)
            age = 1
            print(y)
            sql = 'select "Email","Password","Name" from "Bookticket_customer" where "Email" = %s and "Age">%s'
            print(sql)
            for p in Customer.objects.raw(sql,(email,age)):
                print(p.Email)
                print(p.Password)

            cursor = connection.cursor()
            global username
            username = p.Name
            global valueuser
            valueuser=username
            if Customer.objects.filter(Email=p.Email, Password=p.Password):
                print("login success")
            else:
                print("Login Unsuccessful")


            x=check_password(password,p.Password)
            if x==True:
                print("success")

            return render(request, 'index.html',{'username':username})

            print("failed")
            return render(request, 'login.html')
            user = authenticate(request, Phone=phone, Password=password)
            if user is not None:
                return render(request, 'index.html')
            else:
                form = AuthenticationForm()
                return render(request, 'booknow.html', {'form': form})

    else:
        form = AuthenticationForm()
        return render(request, 'login.html', {'form': form})


def getusername():
    usern=username
    return usern

def myticket(request):
    return render(request, 'mytickets.html')



class BooktickView(TemplateView):
    template_name = "template/bookticket.html"


class Homeview(TemplateView):
    template_name = "template/index.html"


class Trainview(TemplateView):
    template_name = "template/train.html"


from datetime import date

today = date.today()


def booknow(request):
    return render(request, 'booknow.html')


def Timeme(request):
    return render(request, 'bookticket.html')


def train(request):
    if request.method == 'POST':
        dateinput = request.POST.get('dateinput')
        sourceinput = request.POST.get('sourceinput')
        destinput = request.POST.get('destinput')
        print("Hello")
        lfare=[]
        lroute=[]
        ltrainid=[]
        ltrainname=[]
        larrival=[]
        ldepart=[]
        sql='select * from "Bookticket_routes" where "source"=%s and "destination"=%s;'
        for p in Routes.objects.raw(sql, (sourceinput, destinput)):
            print(p.fare)
            lfare.append(p.fare)
            print(p.Route_id)
            lroute.append(p.Route_id)
        route=p.Route_id
        fare=p.fare
        yy=0
        sql1='select * from "Bookticket_trains" where "Route_id_id"=%s and "Time_id_id"!=%s;'
        for r in Trains.objects.raw(sql1, (route,yy)):
            print(r.Train_id)
            ltrainid.append(r.Train_id)
            print(r.Train_name)
            ltrainname.append(r.Train_name)
        ttime = r.Time_id_id
        trainid=r.Train_id
        sql2='select * from "Bookticket_schedule" where "Train_id_id"=%s and "date"=%s;'
        for q in Schedule.objects.raw(sql2, (trainid, dateinput)):
            print(f"q : {q}")
        '''
        sql4 = 'select * from "Bookticket_trains" where "Train_id"=%s and "Time_id_id"!=%s;'
        for a in Trains.objects.raw(sql4, (trainid,yy)):
            '''
        Trainname=r.Train_name
        ldetails=list(itertools.zip_longest(lfare, lroute, ltrainname, ltrainid,larrival,ldepart))
        for (f, r, idd, t) in (itertools.zip_longest(lfare, lroute, ltrainid, ltrainname)):
            newtrain=t
            finalid=r
            print(r)
        print("hey")
    print("oiii")
    return render(request, 'train.html',{'ldetails':ldetails,'sourceinput':sourceinput,'destinput':destinput,'route':route,'Trainname':Trainname,'dateinput':dateinput,'fare':fare,'lfare':lfare,'lroute':lroute,'ltrainid':ltrainid,'ltrainname':ltrainname})


def createpost(request):
    return render(request, 'bookticket.html')




'''
select * from "Bookticket_time" where "Time_id"=(select "Time_id_id" from "Bookticket_trains" where "Train_id" in(select "Train_id" from "Bookticket_schedule" where "date"='2021-09-08')and "Route_id_id"=(select "Route_id" from "Bookticket_routes" where "source"='Goa' and "destination"='Delhi'));
'''