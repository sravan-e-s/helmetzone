from django.urls import path
from User import views
app_name="user"

urlpatterns = [
    path('home/',views.Homepage,name="home"),
    path('profile/',views.MyProfile,name="profile"),
    path('editprof/<int:eid>',views.editProfile,name="editprofile"),
    path('changepass/<int:cid>',views.Changepass,name="changepass"),
    path('search/',views.Searchproduct,name="search"),
    path('ajaxplace/',views.Ajaxplace2,name="Ajax-place"),
    path('ajaxproduct/',views.Ajaxproduct,name="Ajax-product"),
    path('addtocart/<int:pid>',views.Addtocart,name="Addtocart"),
    path('mycart/',views.mycart,name="myCart"),
    path('myOrder/',views.MyOrder,name="Myorder"),
    path('cancelOrder<int:boid>/',views.Cancelorder,name="cancelbooking"),
    path('getqnty/',views.get_qnty,name="GetQty"),
    path('payment/',views.PAYMENT,name="payment"),
    path("complaintt/",views.compl,name="complaint"),
    path('processingpayment/',views.processingpayment,name="processingpayment"),
    path('patmentsucessful/',views.paysucess,name="patmentsucessful"),
    path("feeedback/",views.feedb,name="fedback"),
    path("Viewgallery/<int:pid>",views.ViewGallery,name="Viewgallery"),
    path('logout/',views.logout,name="logout")
]