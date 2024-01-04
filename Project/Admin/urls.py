from django.urls import path
from Admin import views
app_name="webadmin"
urlpatterns = [
    path('dis/',views.district,name="dis"),
    path('deldis/<int:did>',views.deldis,name="deldistrict"),
    path('editdis/<int:did>',views.editdis,name="editdistrict"),
    path('place/',views.place,name="place"),
    path('delplace/<int:pl>',views.delplace,name="delplace"),
    path('brand/',views.brands,name="brn"),
    path('delbr/<int:bid>',views.delbrand,name="delbarandname"),
    path('editbr/<int:bid>',views.editbrand,name="editbrandname"),
    path('model/',views.Helmetmodels,name="models"),
    path('deletemodel/<int:mod>',views.delmodel,name="delemodel"),
    path('sellist/',views.Sellerlist,name="newsellerlist"),
    path('acclist/',views.Acclist,name="accepttedlist"),
    path('rejlist/',views.Rejlist,name="rejectedlist"),
    path('acclist/<int:aid>',views.Acceptseller,name="acceptseller"),
    path('rejlist/<int:rid>',views.Rejectseller,name="rejectseller"),
    path('usrlist/',views.Userlist,name="userlist"),
    path('homee/',views.Adminhome,name="homee"),
    path('vfeedback/',views.FEEDBACK,name="viewfeedback"),
    path('vcomplaint/',views.COMPLAINT,name="viewcomplaint"),
    path('replaycomplaints/<int:cid>',views.REPLAY,name="replay"),
    path('userdata/<int:did>',views.UserDetails,name="Viewuserdetails"),
    path('sellerdata/<int:did>',views.SellerDetails,name="sellerdetails"),
    path('logout/',views.logout,name="logout")
]