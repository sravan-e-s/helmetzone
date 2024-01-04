from django.shortcuts import render,redirect
from Guest.models import *
from Admin.models import *
from Seller.models import *

# Create your views here.
def DeleveyBoy(request):
    if 'did' in request.session:
        return render(request,"Deleveryboy/dHome.html")
    else:
        return redirect("Guest:login")


def DProfile(request):
    if 'did' in request.session:
        photo=Delevery.objects.get(id=request.session['did'])
        return render(request,"Deleveryboy/Dprofile.html",{'d':photo})
    else:
        return redirect("Guest:login")

def Editdboy(request,edid):
    if 'did' in request.session:
        photo=Delevery.objects.get(id=edid)
        if request.method=="POST":
            photo.name=request.POST.get('txtname1')
            photo.contact=request.POST.get('txtcontact1')
            photo.email=request.POST.get('txtemail1')
            photo.address=request.POST.get('txtaddress1')
            photo.save()
            return redirect("delevery:dprofile")
        else:    
            return render(request,"Deleveryboy/dedit.html",{'dat':photo})
    else:
        return redirect("Guest:login")
    


def Changepassdboy(request,cdid):
    if 'did' in request.session:
        change=Delevery.objects.get(id=cdid)
        if request.method=="POST":
            psw=change.password
            old=request.POST.get('Cpass1')
            if old != psw:
                error="Password Not Correct!!"
                return render(request,"User/Changepassword.html",{'ERR':error})
            else:
                change=Delevery.objects.get(id=cdid)
                new=request.POST.get('Npass1')
                change.password=new
                change.save()
                return redirect('Guest:login')
        else:
            return render(request,"Deleveryboy/Cpassdboy.html")
    else:
        return redirect("Guest:login")
    
def AsignedList(request):
    if 'did' in request.session:
        dboys=Delevery.objects.get(id=request.session["did"])
        pdt=Workassign.objects.filter(dboy=dboys,status=0)
        return render(request,"Deleveryboy/AssignedList.html",{'Pdt':pdt})
    else:
        return redirect("Guest:login")


def completebook(request,cid):
    if 'did' in request.session:
        wassign=Workassign.objects.get(id=cid)
        cdid=wassign.cid.id
        cart=Cart.objects.get(id=cdid)
        bid=cart.booking.id
        wassign.status=1
        wassign.save()
        book=Booking.objects.get(id=bid)
        book.booking_status=6
        book.save()
        return redirect("delevery:dhome")
    else:
        return redirect("Guest:login")

def CompletedList(request):
    if 'did' in request.session:
        dboys=Delevery.objects.get(id=request.session["did"])
        pdt=Workassign.objects.filter(dboy=dboys,status=1)
        return render(request,"Deleveryboy/CompletedList.html",{'Pdt':pdt})
    else:
        return redirect("Guest:login")
    


def logout(request):
    del request.session["did"]
    return redirect("Guest:Home")