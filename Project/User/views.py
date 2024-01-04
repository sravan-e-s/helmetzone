from django.shortcuts import render,redirect
from Guest.models import *
from Seller.models import *
from User.models import *
# Create your views here.
def Homepage(request):
    if 'uid' in request.session:
        return render(request,"User/Homepage.html")
    else:
        return redirect("Guest:login")


def MyProfile(request):
    if 'uid' in request.session:
        photo=newuser.objects.get(id=request.session['uid'])
        return render(request,"User/Myprofile.html",{'p':photo})
    else:
        return redirect("Guest:login")


def editProfile(request,eid):
    if 'uid' in request.session:
        photo=newuser.objects.get(id=eid)
        if request.method=="POST":
            photo.name=request.POST.get('txtname')
            photo.contact=request.POST.get('txtcontact')
            photo.email=request.POST.get('txtemail')
            photo.address=request.POST.get('txtaddress')
            photo.save()
            return redirect("user:profile")
        else:    
            return render(request,"User/Editprofile.html",{'data':photo})
    else:
        return redirect("Guest:login")


def Changepass(request,cid):
    if 'uid' in request.session:
        change=newuser.objects.get(id=cid)
        if request.method=="POST":
            psw=change.password
            old=request.POST.get('Cpass')
            if old != psw:
                error="Password Not Correct!!"
                return render(request,"User/Changepassword.html",{'ER':error})
            else:
                change=newuser.objects.get(id=cid)
                new=request.POST.get('Npass')
                change.password=new
                change.save()
                return redirect('Guest:login')
        else:
            return render(request,"User/Changepassword.html")
    else:
        return redirect("Guest:login")


def Searchproduct(request):
    bra=Brand.objects.all()
    mod=helmetModels.objects.all()
    name=productt.objects.all()
    photo=productt.objects.all()
    rate=productt.objects.all()
    if request.method=="POST":
        return render(request,"User/Searchproduct.html",{'bra':bra,'name':name,'photo':photo,'rate':rate})
    else:
        return render(request,"User/Searchproduct.html",{'bra':bra,'name':name,'photo':photo,'rate':rate})

def Ajaxplace2(request):
    bra=Brand.objects.get(id=request.GET.get('bran'))
    mod=helmetModels.objects.filter(brand=bra)
    return render(request,"user/ajaxspace2.html",{'mod':mod})

def Ajaxproduct(request):
    if request.GET.get('mid')!="":
        mod=helmetModels.objects.get(id=request.GET.get('mid'))
        prod=productt.objects.filter(model=mod)
        return render(request,"User/AjaxProduct.html",{'name':prod})
    else:
        brand=Brand.objects.get(id=request.GET.get('bid'))
        prod=productt.objects.filter(model__brand=brand)
        return render(request,"User/AjaxProduct.html",{'name':prod})
    
def Addtocart(request,pid):
    photo=productt.objects.all()
    if 'uid' in request.session:
        message=""
        prod=productt.objects.get(id=pid)
        userid=newuser.objects.get(id=request.session["uid"])
        bcount=Booking.objects.filter(user=userid,booking_status=0).count()
        if bcount>0:
            book=Booking.objects.get(user=userid,booking_status=0)
            id=book.id
            bc=Booking.objects.get(id=id)
            bpcount=Cart.objects.filter(booking=bc,product=prod).count()
            if bpcount>0:
                message="AlreadyAddedtoCart"
                return render(request,"User/Searchproduct.html",{"mess":message,'name':photo})
            else:
                Cart.objects.create(product=prod,booking=bc)
                message="AddedtoCart"
                return render(request,"User/Searchproduct.html",{"mess":message,'name':photo})
        else:
            Booking.objects.create(user=userid)
            bid=Booking.objects.filter(user=userid,booking_status=0).count()
            if bid>0:
                b=Booking.objects.get(user=userid,booking_status=0)
                ids=b.id
                bc=Booking.objects.get(id=ids)
                Cart.objects.create(booking=bc,product=prod)
                message="AddedtoCart"
                return render(request,"User/Searchproduct.html",{"mess":message,'name':photo})
            else:
                return render(request,"User/Searchproduct.html",{"mess":message,'name':photo})
    else:
        return redirect("Guest:login")


def mycart(request):
    if 'uid' in request.session:
        userid=newuser.objects.get(id=request.session["uid"])
        if request.method=="POST":
            return redirect("user:payment")
        else:
            bcount=Booking.objects.filter(user=userid,booking_status=0).count()
            if bcount>0:
                bid=Booking.objects.get(user=userid,booking_status=0)
                ids=bid.id
                request.session["bookingsid"]=ids
                bc=Booking.objects.get(id=ids)
                cartob=Cart.objects.filter(booking=bc)
                return render(request,"User/Mycart.html",{'data':cartob})
            else:
                return render(request,"User/Mycart.html")
    else:
        return redirect("Guest:login")
    
def MyOrder(request):
    if 'uid' in request.session:
        usrid=newuser.objects.get(id=request.session["uid"])
        prdt=Cart.objects.filter(booking__user=usrid,booking__booking_status__gt=1)
        return render(request,"User/myorders.html",{'Prdt':prdt})
    else:
        return redirect("Guest:login")

def Cancelorder(request,boid):
    if 'uid' in request.session:
        bid=Booking.objects.get(id=boid)
        bid.booking_status=4
        bid.save()
        return redirect("user:Myorder")
    else:
        return redirect("Guest:login")


def get_qnty(request):
    if 'uid' in request.session:
        qty=request.GET.get('QTY')
        alt=request.GET.get('ALT')
        cart=Cart.objects.get(id=alt)
        cart.booking_quantity=qty
        cart.save()
        return redirect('user:myCart')
    else:
        return redirect("Guest:login")


def PAYMENT(request):
    if 'uid' in request.session:
        if request.method=="POST": 
            ids=Booking.objects.get(id=request.session["bookingsid"])
            ids.booking_status=1
            ids.save()
            return redirect("user:processingpayment")
        else:
            return render(request,"User/Payment.html")
    else:
        return redirect("Guest:login")
    
    
def compl(request):
    if 'uid' in request.session:
        ab=Complaint.objects.filter(user__gt=0)
        uerid=int(request.session["uid"])
        if request.method=="POST":
            Complaint.objects.create(complaint_title=request.POST.get('title'),content=request.POST.get('content'),user=uerid)
            return render(request,"User/Complaint.html",{'ab':ab})
        else:
            return render(request,"User/Complaint.html",{'ab':ab})
    else:
        return redirect("Guest:login")
    

def processingpayment(request):
    if 'uid' in request.session:
        return render(request,"User/runpayment.html")
    else:
        return redirect("Guest:login")
    

def paysucess(request):
    if 'uid' in request.session:
        return render(request,"User/paysucessful.html")
    else:
        return redirect("Guest:login")

def feedb(request):
    if 'uid' in request.session:
        userid=int(request.session["uid"])
        if request.method=="POST":
            Feedback.objects.create(feedback=request.POST.get('feed'),user=userid)
            return render(request,"User/feedback.html")
        else:
            return render(request,"User/feedback.html")
    else:
        return redirect("Guest:login")
    




def logout(request):
    del request.session["uid"]
    return redirect("Guest:Home")

def ViewGallery(request,pid):
    prod=productt.objects.get(id=pid)
    datas=gallery.objects.filter(product=prod)
    return render(request,"User/ViewGallery.html",{'data':datas})