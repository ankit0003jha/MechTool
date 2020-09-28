from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages
from django.http import HttpResponse
from .models import tools
from .models import contact
from .models import Handtool1
from .models import Powertool1
from .models import Measuringtool1
from .models import Machinetool1
from .models import Automotivetool1
import operator
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from .decorators import unauthenticated_user
from django.contrib.auth import authenticate, login, logout

# Create your views here.


@unauthenticated_user
def index(request):
    return render(request, 'index.html', {'name': 'kiTaNs.com'})


@unauthenticated_user
def about(request):
    return render(request, 'about.html')


@unauthenticated_user
def contacts(request):

    if request.method == "POST":
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        content = request.POST['content']
        print(name, email, phone, content)
        if len(name) < 3 or len(email) < 3 or len(phone) < 10 or len(content) < 4:
            messages.error(request, 'Please fill the form correctly')
        else:
            Contact = contact(name=name, email=email,
                              phone=phone, content=content)
            Contact.save()
            messages.success(
                request, name + ',' + ' Your message has been succesfully sent. Thankyou for ur query ')
    return render(request, 'contact.html')


@login_required(login_url='/')
def home(request):
    return render(request, 'home.html')


@ login_required(login_url='/')
def machtool(request):

    la = Machinetool1.objects.all()

    return render(request, 'machtool.html', {'la': la})


@ login_required(login_url='/')
def autotool(request):

    at = Automotivetool1.objects.all()

    return render(request, 'autotool.html', {'at': at})


@ login_required(login_url='/')
def powertool(request):

    pt = Powertool1.objects.all()

    return render(request, 'powertool.html', {'pt': pt})


@ login_required(login_url='/')
def measuringtool(request):

    mt = Measuringtool1.objects.all()

    return render(request, 'measuringtool.html', {'mt': mt})


@ login_required(login_url='/')
def handtool1(request):

    ht = Handtool1.objects.all()

    return render(request, 'handtool1.html', {'ht': ht})


@ login_required(login_url='/')
def hammer(request):
    return render(request, 'hammer.html')


@ login_required(login_url='/')
def blockplane(request):
    return render(request, 'blockplane.html')


@ login_required(login_url='/')
def pliers(request):
    return render(request, 'pliers.html')


@ login_required(login_url='/')
def screw(request):
    return render(request, 'screw.html')


@ login_required(login_url='/')
def wrench(request):
    return render(request, 'wrench.html')


@ login_required(login_url='/')
def chisel(request):
    return render(request, 'chisel.html')


@ login_required(login_url='/')
def saw(request):
    return render(request, 'saw.html')


@ login_required(login_url='/')
def punch(request):
    return render(request, 'punch.html')


@ login_required(login_url='/')
def file(request):
    return render(request, 'file.html')


@ login_required(login_url='/')
def bench(request):
    return render(request, 'bench.html')


@ login_required(login_url='/')
def hatchet(request):
    return render(request, 'hatchet.html')


@ login_required(login_url='/')
def clamp(request):
    return render(request, 'clamp.html')


def register(request):

    if request.method == 'POST':
        first_name = request.POST['first_name']
        username = request.POST['username']
        password = request.POST['password']
        re_password = request.POST['re_password']
        email = request.POST['email']
        if password == re_password:
            if User.objects.filter(username=username).exists():
                messages.error(request, 'Username Taken')
                return redirect("/")
            elif User.objects.filter(email=email).exists():
                messages.error(
                    request, 'This Email-id has been registered before')
                return redirect('/')
            if len(password) < 5:
                messages.error(
                    request, 'password is not strong (must have 5 or more character)')
            else:
                user = User.objects.create_user(
                    username=username, password=re_password, email=email, first_name=first_name)
                user.save()
                messages.success(
                    request, 'You have been succesfully registered, Please login to ur account ')
                print('user created')
                return redirect('/')
        else:

            messages.error(request, 'password not matching')

            return redirect('/')
        return redirect('/')

    else:
        return render(request, 'index.html')


def loginuser(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect("/home")

        else:
            messages.error(
                request, 'Username or Password is invalid! Try-again')
            return redirect('/')
    else:
        return render(request, '/')


@ login_required(login_url='/')
def search(request):
    query = request.GET['query']
    # ts = Tools.objects.all()
    if len(query) > 50 or len(query) == 0:
        ts = []

        messages.warning(
            request, 'No search result found. Please refine your query')
    else:
        ts = tools.objects.filter(name__icontains=query)
        ht = Handtool1.objects.filter(name__icontains=query)
        pt = Powertool1.objects.filter(name__icontains=query)
        mt = Measuringtool1.objects.filter(name__icontains=query)
        la = Machinetool1.objects.filter(name__icontains=query)
        at = Automotivetool1.objects.filter(name__icontains=query)

    params = {'ts': ts, 'query': query, 'ht': ht,
              'pt': pt, 'mt': mt, 'la': la, 'at': at}
    return render(request, 'search.html', params)


@ login_required(login_url='/')
def handtool(request):

    ts = tools.objects.all()

    return render(request, 'handtool.html', {'ts': ts})


def logoutuser(request):
    logout(request)
    return redirect('index')
