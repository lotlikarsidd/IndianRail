from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.views.decorators.csrf import csrf_protect
from pyexpat.errors import messages
from django.contrib.auth import authenticate,login as django_login, logout as django_logout
from Bookticket.models import Customer
from collections import OrderedDict
from datetime import datetime
import itertools
from django.contrib import messages



from .models import Customer,Routes, Trains, Schedule, Time as timetrain
from django.contrib.auth.hashers import make_password, check_password
# Create your views here.


# def home(request):
#   return render(request, 'index.html', {})


from django.shortcuts import render
from django.views.generic.base import TemplateView


# Create your views here.
global page
page=0


def home(request):
    return render(request, 'index.html')


def booktick(request):

    images=[]
    images.append(1);
    images.append(2);
    images.append(3);


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
    return render(request, 'bookticket.html',{'sourcelist':sourcelist,'destlist':destlist,'today':today, 'images':images})





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


from django.contrib.auth.forms import AuthenticationForm

from django.db import connection



def logout(request):
    # Log out the user.
    django_logout(request)
    # Return to homepage.
    return render(request, 'index.html')



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
                user = authenticate(request, username=email, password=password)
                if(authenticate(request, email=email, password=p.Password)):
                    print("loggedin")
                django_login(request, user)



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
    if request.method == 'POST':
        p_age = request.POST.get("page")
        name = request.POST.get('name')
        route = request.POST.get('route')
        arrival = request.POST.get('arrival')
        source = request.POST.get('source')
        date= request.POST.get('date')
        dest = request.POST.get('dest')
        depart = request.POST.get('depart')
        count = request.POST.get('count')
        page = request.POST.get('page')



        return render(request, 'booknow.html',{'name':name,'route':route,'arrival':arrival,'source':source,'date':date,'dest':dest,'depart':depart})



        # CancelFromTrain("S3",36,180,0,30)

        # Initializing the train





def Timeme(request):
    return render(request, 'bookticket.html')


def train(request):
    try:
        if request.method == 'POST':
            dateinput = request.POST.get('dateinput')
            sourceinput = request.POST.get('sourceinput')
            destinput = request.POST.get('destinput')
            print("Hello")
            lfare = []
            lroute = []
            ltrainid = []
            ltrainname = []
            larrival = []
            ldepart = []
            sql = 'select * from "Bookticket_routes" where "source"=%s and "destination"=%s;'
            for p in Routes.objects.raw(sql, (sourceinput, destinput)):
                print(p.fare)
                lfare.append(p.fare)
                print(p.Route_id)
                lroute.append(p.Route_id)
            route = p.Route_id
            fare = p.fare
            yy = 0

            sql1 = 'select * from "Bookticket_trains" where "Route_id_id"=%s and "Time_id_id"!=%s;'
            for r in Trains.objects.raw(sql1, (route, yy)):
                print(r.Train_id)
                ltrainid.append(r.Train_id)
                print(r.Train_name)
                ltrainname.append(r.Train_name)
                print("*")
                trainid = r.Train_id
                if trainid == "KON17GABN":
                    larrival.append("14:00")
                    ldepart.append("15:00")
                    print(larrival)
                elif trainid == "SHA19GADL":
                    larrival.append("18:00")
                    ldepart.append("19:00")
                    print(larrival)
                elif trainid == "KON12GADL":
                    larrival.append("11:00")
                    ldepart.append("12:00")
                    print(larrival)
                elif trainid == "RAJ17AMGA":
                    larrival.append("14:00")
                    ldepart.append("15:00")
                    print(larrival)
                else:
                    larrival.append("21:00")
                    ldepart.append("22:00")
                    print(larrival)
            print("1")
            sql2 = 'select * from "Bookticket_trains" where "Train_id"=%s and "Time_id_id"!=%s'
            for q in Trains.objects.raw(sql2, (trainid, yy)):
                print(q.Train_name)
                print(q)
            print("2")
            sql6 = 'select * from "Bookticket_time" where "Time_id"=%s and "Arrival_Time"!=%s'
            for i in timetrain.objects.raw(sql6, (r.Time_id_id, str(yy))):
                print(i.Arrival_Time, "hellooooo")
                print(i.Departure_Time)
            Trainname = r.Train_name
            ldetails = list(itertools.zip_longest(ltrainname, ltrainid, larrival, ldepart))
            for (f, r, idd, t) in (itertools.zip_longest(lfare, lroute, ltrainid, ltrainname)):
                print(r)
            print("hey")
            print("oiii")
            return render(request, 'train.html',
                          {'ldetails': ldetails, 'sourceinput': sourceinput, 'destinput': destinput, 'route': route,
                           'Trainname': Trainname, 'dateinput': dateinput, 'fare': fare})
    except:
        return render(request, 'error.html')

def createpost(request):
    return render(request, 'bookticket.html')

def confirm(request):
    global page
    page=request.POST.get("page")

    class Train:
        No_of_compartments = 5
        No_of_Seats = 72
        No_of_Berths = 2
        No_of_SeatsReserved = int(6 * No_of_compartments)
        AvailableLowerBerth = int(((No_of_Seats * No_of_compartments) / No_of_Berths) - No_of_SeatsReserved)
        AvailableUpperBerth = int((No_of_Seats * No_of_compartments) / No_of_Berths)
        AvailableReserved = No_of_SeatsReserved
        LowerBerth = []
        UpperBerth = []
        Reserved = []
        CanceledUpper = []
        CanceledLower = []

        def IntializeSeats(self):

            # Lower Berth

            leftFromCentreForLower = 22
            RightFromCentreForLower = 51

            for x in range(0, 15):
                self.LowerBerth.append('S5 ' + str(RightFromCentreForLower))
                self.LowerBerth.append('S5 ' + str(leftFromCentreForLower))
                self.LowerBerth.append('S1 ' + str(RightFromCentreForLower))
                self.LowerBerth.append('S1 ' + str(leftFromCentreForLower))
                self.LowerBerth.append('S4 ' + str(RightFromCentreForLower))
                self.LowerBerth.append('S4 ' + str(leftFromCentreForLower))
                self.LowerBerth.append('S2 ' + str(RightFromCentreForLower))
                self.LowerBerth.append('S2 ' + str(leftFromCentreForLower))
                self.LowerBerth.append('S3 ' + str(RightFromCentreForLower))
                self.LowerBerth.append('S3 ' + str(leftFromCentreForLower))
                leftFromCentreForLower = leftFromCentreForLower + 1
                RightFromCentreForLower = RightFromCentreForLower - 1

            # Upper Berth

            leftFromCentreForUpper = 1
            RightFromCentreForUpper = 72

            for x in range(0, 18):
                self.UpperBerth.append('S5 ' + str(RightFromCentreForUpper))
                self.UpperBerth.append('S5 ' + str(leftFromCentreForUpper))
                self.UpperBerth.append('S1 ' + str(RightFromCentreForUpper))
                self.UpperBerth.append('S1 ' + str(leftFromCentreForUpper))
                self.UpperBerth.append('S4 ' + str(RightFromCentreForUpper))
                self.UpperBerth.append('S4 ' + str(leftFromCentreForUpper))
                self.UpperBerth.append('S2 ' + str(RightFromCentreForUpper))
                self.UpperBerth.append('S2 ' + str(leftFromCentreForUpper))
                self.UpperBerth.append('S3 ' + str(RightFromCentreForUpper))
                self.UpperBerth.append('S3 ' + str(leftFromCentreForUpper))
                leftFromCentreForUpper = leftFromCentreForUpper + 1
                RightFromCentreForUpper = RightFromCentreForUpper - 1

            # Reserved

            self.Reserved.append('S5 ' + str(54))
            self.Reserved.append('S5 ' + str(19))
            self.Reserved.append('S1 ' + str(54))
            self.Reserved.append('S1 ' + str(19))
            self.Reserved.append('S4 ' + str(54))
            self.Reserved.append('S4 ' + str(19))
            self.Reserved.append('S2 ' + str(54))
            self.Reserved.append('S2 ' + str(19))
            self.Reserved.append('S3 ' + str(54))
            self.Reserved.append('S3 ' + str(19))
            self.Reserved.append('S5 ' + str(53))
            self.Reserved.append('S5 ' + str(20))
            self.Reserved.append('S1 ' + str(53))
            self.Reserved.append('S1 ' + str(20))
            self.Reserved.append('S4 ' + str(53))
            self.Reserved.append('S4 ' + str(20))
            self.Reserved.append('S2 ' + str(53))
            self.Reserved.append('S2 ' + str(20))
            self.Reserved.append('S3 ' + str(53))
            self.Reserved.append('S3 ' + str(20))
            self.Reserved.append('S5 ' + str(52))
            self.Reserved.append('S5 ' + str(21))
            self.Reserved.append('S1 ' + str(52))
            self.Reserved.append('S1 ' + str(21))
            self.Reserved.append('S4 ' + str(52))
            self.Reserved.append('S4 ' + str(21))
            self.Reserved.append('S2 ' + str(52))
            self.Reserved.append('S2 ' + str(21))
            self.Reserved.append('S3 ' + str(52))
            self.Reserved.append('S3 ' + str(21))

        # Ticket Booking
        def Book_Ticket(self, Age):
            seatno = []
            Berth = [" LOWER "]
            self.AvailableLowerBerth = self.AvailableLowerBerth - 1
            if Age > 64:
                if (len(self.CanceledLower)):
                    seatno.append(self.CanceledLower.pop())
                elif (len(self.LowerBerth)):
                    seatno.append(self.LowerBerth.pop())
                elif (len(self.Reserved)):
                    seatno.append(self.Reserved.pop())
                    self.AvailableReserved = self.AvailableReserved - 1
                    self.AvailableLowerBerth = self.AvailableLowerBerth + 1
                else:
                    seatno.append("No Seat Available")
                    self.AvailableLowerBerth = self.AvailableLowerBerth + 1
            else:
                if (len(self.CanceledUpper)):
                    seatno.append(self.CanceledUpper.pop())
                    Berth = [" UPPER "]
                    self.AvailableUpperBerth = self.AvailableUpperBerth - 1
                    self.AvailableLowerBerth = self.AvailableLowerBerth + 1
                elif (len(self.UpperBerth)):
                    seatno.append(self.UpperBerth.pop())
                    Berth = [" UPPER "]
                    self.AvailableUpperBerth = self.AvailableUpperBerth - 1
                    self.AvailableLowerBerth = self.AvailableLowerBerth + 1
                elif (len(self.CanceledLower)):
                    seatno.append(self.CanceledLower.pop())
                elif (len(self.LowerBerth)):
                    seatno.append(self.LowerBerth.pop())
                elif (len(self.Reserved)):
                    seatno.append(self.Reserved.pop())
                    self.AvailableReserved = self.AvailableReserved - 1
                    self.AvailableLowerBerth = self.AvailableLowerBerth + 1
                else:
                    self.AvailableLowerBerth = self.AvailableLowerBerth + 1
            return (seatno, Berth[0])

        ''' For Testing only
        def test(self):
            print('\nYour Ticket:')
            for x in range(0,45):
                self.Book_Ticket("abc",68)
                self.Book_Ticket("sdsff",25)
                self.Book_Ticket("hjsh",65)

        '''

        def Booking_Counter(self):
            noOfTickets = int(input("How Many Tickets You want To book "))
            for n in range(0, noOfTickets):
                name = input("Name on Ticket  ")
                age = int(input("Age "))
                self.Book_Ticket(name, age)

        def Cancel_Ticket(self, cno, sno):
            if sno == 19 or sno == 20 or sno == 21 or sno == 52 or sno == 53 or sno == 54:
                self.Reserved.append(cno + " " + str(sno))
                self.AvailableReserved = self.AvailableReserved + 1
                print('Canceled Lower Reserved ')
                print(self.Reserved)
            elif sno > 21 and sno < 52:
                self.CanceledLower.append(cno + " " + str(sno))
                self.AvailableLowerBerth = self.AvailableLowerBerth + 1
                print('Canceled Lower Berth ')
                print(self.CanceledLower)
            else:
                self.CanceldUpper.append(cno + " " + str(sno))
                self.AvailableUpperBerth = self.AvailableUpperBerth + 1
                print('Canceled Upper Berth ')
                print(self.CanceledUpper)

    def BookIntoTrain(age, lCount, UCount, RCount):
        Train1 = Train()
        Train1.IntializeSeats()
        if (lCount != 0):
            for n in range(0, lCount):
                Train1.Book_Ticket(68)
        if (UCount != 0):
            for n in range(0, UCount):
                Train1.Book_Ticket(34)
        if (RCount != 0):
            for n in range(0, RCount):
                Train1.Book_Ticket(63)
        (seatid, berth) = Train1.Book_Ticket(age)
        print(berth)
        tno = str(seatid.pop())
        print(tno)

        del Train1
        # Save the following on the database besides the train
        # Train1.AvailableLowerBerth
        # Train1.AvailableUpperBerth
        # Train1.AvailableReserved

        # save the tno into the passenger ticket no

    def CancelFromTrain(CompNo, Seatno, lCount, UCount, Rcount):
        Train1 = Train()
        Train1.IntializeSeats()
        for n in range(0, lCount):
            Train1.Book_Ticket(68)
        for n in range(0, UCount):
            Train1.Book_Ticket(34)
        for n in range(0, Rcount):
            Train1.Book_Ticket(63)
        Train1.Cancel_Ticket(CompNo, Seatno)
        print("your ticket " + CompNo + " " + str(Seatno) + "is Canceled")
        del Train1

        # Save the following on the database besides the train
        # Train1.AvailableLowerBerth
        # Train1.AvailableUpperBerth
        # Train1.AvailableReserved

        # delete the passenger ID to this ticket number

    # use these funtions to book or cancel ticket
    page=int(page)

    BookIntoTrain(page, 0, 0, 0)  # enter the age and count values
    print("after bookinto call")
    messages.info(request, 'Your password has been changed successfully!')
    '''
    return render(request, 'booknow.html',
                  {'name': name, 'route': route, 'arrival': arrival, 'source': source, 'date': date, 'dest': dest,
                   'depart': depart})
    '''
    return render(request, 'confirmation.html')

from django.shortcuts import render_to_response
from django.template import RequestContext


def handler404(request, *args, **argv):
    response = render_to_response('error.html', {},
                                  context_instance=RequestContext(request))
    response.status_code = 404
    return response


def handler500(request, *args, **argv):
    response = render_to_response('error.html', {},
                                  context_instance=RequestContext(request))
    response.status_code = 500
    return response


