from django.shortcuts import render,redirect
from Guest.models import *
from Admin.models import *
from Seller.models import *
from django.core.mail import send_mail
from django.conf import settings
# Create your views here.
def Newseller(request):
    dis=District.objects.all()
    pl=Place.objects.all()
    if request.method=="POST":
        d=District.objects.get(id=request.POST.get('disid2'))
        pl=Place.objects.get(id=request.POST.get('selplace'))
        Seller.objects.create(name=request.POST.get('name1'),contact=request.POST.get('contact1'),email=request.POST.get('email1'),address=request.POST.get('address1'),place=pl,logo=request.FILES.get('logo1'),proof=request.FILES.get('proof1'),password=request.POST.get('pass1'))
        send_mail(
            'Respected Sir/Madam '+request.POST.get('name1'),#subject
            "Your Account Created SucessFully",#body
            settings.EMAIL_HOST_USER,
            [request.POST.get('email1')],
        )
        return render(request,"Guest/Newseller.html",{'dis':dis})
    else:
        return render(request,"Guest/Newseller.html",{'dis':dis})



def Newuser(request):
    dis=District.objects.all()
    pl=Place.objects.all()
    if request.method=="POST":
        d=District.objects.get(id=request.POST.get('disid2'))
        pl=Place.objects.get(id=request.POST.get('selplace'))
        newuser.objects.create(name=request.POST.get('name2'),contact=request.POST.get('contact2'),email=request.POST.get('email2'),address=request.POST.get('adder2'),place=pl,gender=request.POST.get('gender'),photo=request.FILES.get('file2'),password=request.POST.get('pass2'))
        send_mail(
            'Respected Sir/Madam '+request.POST.get('name2'),#subject
            "Your Account Created SucessFully",#body
            settings.EMAIL_HOST_USER,
            [request.POST.get('email2')],
        )
        return render(request,"Guest/Newuser.html",{'dis':dis})
    else:
        return render(request,"Guest/Newuser.html",{'dis':dis})

def Ajaxplace(request):
    dis=District.objects.get(id=request.GET.get('disd'))
    pl=Place.objects.filter(district=dis)
    return render(request,"Guest/ajaxspace.html",{'pl':pl})
   


def Login(request):
    if request.method=="POST":
        Email=request.POST.get('logemail')
        Pass=request.POST.get('logpass')
        Ulogin=newuser.objects.filter(email=Email,password=Pass).count()
        Slogin=Seller.objects.filter(email=Email,password=Pass,vstatus=True).count()
        Alogin=Admintable.objects.filter(admin_email=Email,admin_password=Pass).count()
        Dlogin=Delevery.objects.filter(email=Email,password=Pass).count()
        if Ulogin > 0:
            uadmin=newuser.objects.get(email=Email,password=Pass)
            request.session['uid']=uadmin.id
            return redirect('user:home')
        elif Slogin > 0:
            sadmin=Seller.objects.get(email=Email,password=Pass,vstatus=1)
            request.session['sid']=sadmin.id
            return redirect('seller:sellhome')
        elif Alogin > 0:
            aadmin=Admintable.objects.get(admin_email=Email,admin_password=Pass)
            request.session['aid']=aadmin.id
            return redirect('webadmin:homee')
        elif Dlogin > 0:
            dadmin=Delevery.objects.get(email=Email,password=Pass)
            request.session['did']=dadmin.id
            return redirect('delevery:dhome')
        else:
            error="Invalid Credentials!!"
            return render(request,"Guest/Login.html",{'ERR':error})
    else:
        return render(request,"Guest/login.html")
    

def homepage(request):
    return render(request,"Guest/Home.html")

def Viewproducts(request):
    pr=productt.objects.all()
    return render(request,"Guest/ViewProducts.html",{'data':pr})