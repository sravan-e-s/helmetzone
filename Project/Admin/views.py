from django.shortcuts import render,redirect
from Admin.models import *
from Guest.models import *
# Create your views here.
def district(request):
    if 'aid' in request.session:
        dis=District.objects.all()
        if request.method=="POST":
            District.objects.create(district_name=request.POST.get('di'))
            return render(request,"Admin/District.html",{'data':dis})
        else:
            return render(request,"Admin/District.html",{'data':dis})
    else:
        return redirect("Guest:login")


def deldis(request,did):
    if 'aid' in request.session:
        dis=District.objects.get(id=did)
        dis.delete()
        return redirect("webadmin:dis")
    else:
        return redirect("Guest:login")

def editdis(request,did):
    if 'aid' in request.session:
        dis=District.objects.get(id=did)
        if request.method=="POST":
            dis.district_name=request.POST.get('diss')
            dis.save()
            return redirect("webadmin:dis")
        else:
            return render(request,"Admin/editdistrict.html",{'data':dis})
    else:
        return redirect("Guest:login")


def place(request):
    if 'aid' in request.session:
        dis=District.objects.all()
        pl=Place.objects.all()
        if request.method=="POST":
            d=District.objects.get(id=request.POST.get('distdrop'))
            Place.objects.create(place_name=request.POST.get('txt1'),district=d)
            return render(request,"Admin/place.html",{'dis':dis,'pl':pl})
        else:
            return render(request,"Admin/place.html",{'dis':dis,'pl':pl})
    else:
        return redirect("Guest:login")

def delplace(request,pl):
    if 'aid' in request.session:
        place=Place.objects.get(id=pl)
        place.delete()
        return redirect("webadmin:place")
    else:
        return redirect("Guest:login")


def brands(request):
    if 'aid' in request.session:
        br=Brand.objects.all()
        if request.method=="POST":
            Brand.objects.create(brand_name=request.POST.get('brand'))
            return render(request,"Admin/brand.html",{'data':br})
        else:
            return render(request,"Admin/brand.html",{'data':br})
    else:
        return redirect("Guest:login")

def delbrand(request,bid):
    if 'aid' in request.session:
        br=Brand.objects.get(id=bid)
        br.delete()
        return redirect("webadmin:brn")
    else:
        return redirect("Guest:login")


def editbrand(request,bid):
    if 'aid' in request.session:
        br=Brand.objects.get(id=bid)
        if request.method=="POST":
            br.brand_name=request.POST.get('brr')
            br.save()
            return redirect("webadmin:brn")
        else:
            return render(request,"Admin/editbrand.html",{'data':br})
    else:
        return redirect("Guest:login")


def Helmetmodels(request):
    if 'aid' in request.session:
        br=Brand.objects.all()
        mod=helmetModels.objects.all()
        if request.method=="POST":
            b=Brand.objects.get(id=request.POST.get('bradrop'))
            helmetModels.objects.create(model_name=request.POST.get('txt'),brand=b)
            return render(request,"Admin/models.html",{'br':br,'mod':mod})
        else:
            return render(request,"Admin/models.html",{'br':br,'mod':mod})
    else:
        return redirect("Guest:login")



def delmodel(request,mod):
    if 'aid' in request.session:
        models=helmetModels.objects.get(id=mod)
        models.delete()
        return redirect("webadmin:models")
    else:
        return redirect("Guest:login")


def Sellerlist(request):
    if 'aid' in request.session:
        se=Seller.objects.filter(vstatus=0)
        return render(request,"Admin/Newsellerlist.html",{'se':se})
    else:
        return redirect("Guest:login")





def Acclist(request):
    if 'aid' in request.session:
        se=Seller.objects.filter(vstatus=1)
        return render(request,"Admin/Accepttedlist.html",{'se':se})
    else:
        return redirect("Guest:login")


def Rejlist(request):
    if 'aid' in request.session:
        se=Seller.objects.filter(vstatus=2)
        return render(request,"Admin/Rejectedlist.html",{'se':se})
    else:
        return redirect("Guest:login")



def Acceptseller(request,aid):
    if 'aid' in request.session:
        se=Seller.objects.get(id=aid)
        se.vstatus=1
        se.save()
        return redirect("webadmin:newsellerlist")
    else:
        return redirect("Guest:login")


def Rejectseller(request,rid):
    if 'aid' in request.session:
        se=Seller.objects.get(id=rid)
        se.vstatus=2
        se.save()
        return redirect("webadmin:newsellerlist")
    else:
        return redirect("Guest:login")

def Userlist(request):
    if 'aid' in request.session:
        us=newuser.objects.all()
        return render(request,"Admin/userlist.html",{'us':us})
    else:
        return redirect("Guest:login")


def Adminhome(request):
    if 'aid' in request.session:
        return render(request,"Admin/Adminhomepage.html")
    else:
        return redirect("Guest:login")


def FEEDBACK(request):
    if 'aid' in request.session:
        abc=Feedback.objects.filter(user__gt=0)
        sellerf=Feedback.objects.filter(seller__gt=0)
        return render(request,"Admin/ViewFeedback.html",{'abc':abc,'sellf':sellerf})
    else:
        return redirect("Guest:login")
    

def COMPLAINT(request):
    if 'aid' in request.session:
        ab=Complaint.objects.filter(user__gt=0,complaint_status=0)
        sellf=Complaint.objects.filter(seller__gt=0,complaint_status=0)
        return render(request,"Admin/viewcomplaints.html",{'ab':ab,'sellf':sellf})
    else:
        return redirect("Guest:login")
    
def REPLAY(request,cid):
    br=Complaint.objects.get(id=cid)
    if request.method=="POST":
            br.complaint_replay=request.POST.get('replay')
            br.complaint_status=1
            br.save()
            return redirect("webadmin:viewcomplaint")
    else:
        return render(request,"Admin/replaytocomplaint.html")



def logout(request):
    del request.session["aid"]
    return redirect("Guest:Home")

def UserDetails(request,did):
    cid=Complaint.objects.get(id=did)
    uid=cid.user
    user=newuser.objects.get(id=uid)
    return render(request,"Admin/ViewUSerData.html",{'s':user})
def SellerDetails(request,did):
    cid=Complaint.objects.get(id=did)
    sid=cid.seller
    user=Seller.objects.get(id=sid)
    return render(request,"Admin/vIewSeller.html",{'s':user})