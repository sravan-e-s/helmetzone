from django.shortcuts import render,redirect
from Guest.models import *
from Admin.models import *
from Seller.models import *
from User.models import Cart

# Create your views here.
def Sellerhome(request):
    if 'sid' in request.session:
        return render(request,"Seller/sellerhomepage.html")
    else:
        return redirect("Guest:login")


def SellerProfile(request):
    if 'sid' in request.session:
        logo=Seller.objects.get(id=request.session['sid'])
        return render(request,"Seller/Sellerprofile.html",{'s':logo})
    else:
        return redirect("Guest:login")


def editSeller(request,esid):
    if 'sid' in request.session:
        logo=Seller.objects.get(id=esid)
        if request.method=="POST":
            logo.name=request.POST.get('txtname1')
            logo.contact=request.POST.get('txtcontact1')
            logo.email=request.POST.get('txtemail1')
            logo.address=request.POST.get('txtaddress1')
            logo.save()
            return redirect("seller:Sellprofile")
        else:    
            return render(request,"Seller/Selleredit.html",{'dat':logo})
    else:
        return redirect("Guest:login")



def Changepassseller(request,sid):
    if 'sid' in request.session:
        change=Seller.objects.get(id=sid)
        if request.method=="POST":
            psw=change.password
            old=request.POST.get('Cpass1')
            if old != psw:
                error="Password Not Correct!!"
                return render(request,"User/Changepassword.html",{'ERR':error})
            else:
                change=Seller.objects.get(id=sid)
                new=request.POST.get('Npass1')
                change.password=new
                change.save()
                return redirect('Guest:login')
        else:
            return render(request,"Seller/Cpassseller.html")
    else:
        return redirect("Guest:login")


def Deleveryboy(request):
    if 'sid' in request.session:
        sdid=Seller.objects.get(id=request.session['sid'])
        dis=District.objects.all()
        pl=Place.objects.all()
        delivery=Delevery.objects.filter(seller=sdid)
        sid=Seller.objects.filter(vstatus=1)
        if request.method=="POST":
            pl=Place.objects.get(id=request.POST.get('Dselplace'))
            Delevery.objects.create(name=request.POST.get('Dname'),contact=request.POST.get('Dcontact'),email=request.POST.get('Demail'),address=request.POST.get('Dadder'),place=pl,photo=request.FILES.get('Dfile'),password=request.POST.get('Dpass'),seller=sdid)
            return render(request,"Seller/Deliveryboy.html",{'dis':dis,'dboy':delivery})
        else:
            return render(request,"Seller/Deliveryboy.html",{'dis':dis,'dboy':delivery})
    else:
        return redirect("Guest:login")

def delDboy(request,did):
    if 'sid' in request.session:
        dboy=Delevery.objects.get(id=did)
        dboy.delete()
        return redirect("seller:delevery")
    else:
        return redirect("Guest:login")



def Product(request):
    if 'sid' in request.session:
        slid=Seller.objects.get(id=request.session['sid'])
        bra=Brand.objects.all()
        mod=helmetModels.objects.all()
        hel=productt.objects.filter(seller=slid)
        sid=Seller.objects.filter(vstatus=1)
        if request.method=="POST":
            pl=helmetModels.objects.get(id=request.POST.get('model'))
            productt.objects.create(name=request.POST.get('Pname'),photo=request.FILES.get('Pphoto'),rate=request.POST.get('Prate'),details=request.POST.get('Pdetails'),model=pl,seller=slid)
            return render(request,"Seller/Product.html",{'bra':bra,'hel':hel})
        else:
            return render(request,"Seller/Product.html",{'bra':bra,'hel':hel})
    else:
        return redirect("Guest:login")

def Ajaxplace1(request):
    if 'sid' in request.session:
        bra=Brand.objects.get(id=request.GET.get('bran'))
        mod=helmetModels.objects.filter(brand=bra)
        return render(request,"seller/ajaxspace1.html",{'mod':mod})
    else:
        return redirect("Guest:login")

def delPdt(request,mid):
    if 'sid' in request.session:
        dpdt=productt.objects.get(id=mid)
        dpdt.delete()
        return redirect("seller:product")
    else:
        return redirect("Guest:login")

def Bookking(request):
    if 'sid' in request.session:
        sell=Seller.objects.get(id=request.session["sid"])
        pdt=Cart.objects.filter(product__seller=sell,booking__booking_status=1)
        return render(request,"Seller/Viewbookings.html",{'Pdt':pdt})
    else:
        return redirect("Guest:login")


def Acceptbooking(request,aid):
    if 'sid' in request.session:
        bid=Booking.objects.get(id=aid)
        bid.booking_status=3
        bid.save()
        return redirect("seller:viewbookings")
    else:
        return redirect("Guest:login")

def Rejectbooking(request,rid):
    if 'sid' in request.session:
        bid=Booking.objects.get(id=rid)
        bid.booking_status=4
        bid.save()
        return redirect("seller:viewbookings")
    else:
        return redirect("Guest:login")

def Acclist(request):
    if 'sid' in request.session:
        sell=Seller.objects.get(id=request.session["sid"])
        pdt=Cart.objects.filter(product__seller=sell,booking__booking_status=3)
        return render(request,"Seller/acceptOrder.html",{'Pdt':pdt})
    else:
        return redirect("Guest:login")
   

def Rejlist(request):
    if 'sid' in request.session:
        sell=Seller.objects.get(id=request.session["sid"])
        pdt=Cart.objects.filter(product__seller=sell,booking__booking_status=4)
        return render(request,"Seller/rejOrder.html",{'Pdt':pdt})
    else:
        return redirect("Guest:login")

def Assignorder(request,eid):
    if 'sid' in request.session:
        cid=Cart.objects.get(id=eid)
        bid=cid.booking.id
        request.session["booking"]=bid
        selll=Seller.objects.get(id=request.session["sid"])
        delivery=Delevery.objects.filter(seller=selll)
        return render(request,"Seller/Assign.html",{'Ddboy':delivery})
    else:
        return redirect("Guest:login")

def Assign(request,did):
    if 'sid' in request.session:
        dboys=Delevery.objects.get(id=did)
        print(request.session["booking"])
        bookings=Booking.objects.get(id=request.session["booking"])
        ccount=Cart.objects.filter(booking=bookings).count()
        for i in range(ccount):
            cd=Cart.objects.filter(booking=bookings)[i]
            Workassign.objects.create(dboy=dboys,cid=cd)
        bookings.booking_status=5
        bookings.save()
        return redirect("seller:sellhome")
    else:
        return redirect("Guest:login")

def AsignedList(request):
    if 'sid' in request.session:
        sell=Seller.objects.get(id=request.session["sid"])
        pdt=Cart.objects.filter(product__seller=sell,booking__booking_status__gte=5)
        return render(request,"Seller/AssignedList.html",{'Pdt':pdt})
    else:
        return redirect("Guest:login")
    
def FEED(request):
    if 'sid' in request.session:
        selleid=int(request.session["sid"])
        if request.method=="POST":
            Feedback.objects.create(feedback=request.POST.get('feeed'),seller=selleid)
            return render(request,"Seller/sentfeedback.html")
        else:
            return render(request,"Seller/sentfeedback.html")
    else:
        return redirect("Guest:login")
    

def COMP(request):
    if 'sid' in request.session:
        sellf=Complaint.objects.filter(seller__gt=0)
        selid=int(request.session["sid"])
        if request.method=="POST":
            Complaint.objects.create(complaint_title=request.POST.get('title1'),content=request.POST.get('content1'),seller=selid)
            return render(request,"Seller/sntcomplaint.html",{'sellf':sellf})
        else:
            return render(request,"Seller/sntcomplaint.html",{'sellf':sellf})
    else:
        return redirect("Guest:login")


def logout(request):
    del request.session["sid"]
    return redirect("Guest:Home")

def Gallery(request,did):
    pid=productt.objects.get(id=did)
    if request.method=="POST":
        gallery.objects.create(product=pid,images=request.FILES.get('gimage'))
        return redirect("seller:product")
    else:
        return render(request,"Seller/gallery.html")