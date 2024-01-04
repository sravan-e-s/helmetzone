from django.urls import path
from Seller import views
app_name="seller"
urlpatterns = [
    path('sellhome/',views.Sellerhome,name="sellhome"),
    path('sellprofile/',views.SellerProfile,name="Sellprofile"),
    path('editseller/<int:esid>',views.editSeller,name="editseller"),
    path('changepassseller/<int:sid>',views.Changepassseller,name="changepassseller"),
    path('delevery/',views.Deleveryboy,name="delevery"),
    path('deldboy/<int:did>',views.delDboy,name="deldboy"),
    path('product/',views.Product,name="product"),
    path('ajaxplace/',views.Ajaxplace1,name="Ajax-place"),
    path('delproduct/<int:mid>',views.delPdt,name="delpdt"),
    path('viewbookings/',views.Bookking,name="viewbookings"),
    path('acceptbooking/<int:aid>',views.Acceptbooking,name="acceptorder"),
    path('rejectbooking/<int:rid>',views.Rejectbooking,name="rejectorder"),
    path('acceptedlist/',views.Acclist,name="acclist"),
    path('rejectedlist/',views.Rejlist,name="rejlist"),
    path('assign/<int:eid>',views.Assignorder,name="assignorder"),
    path('assigndelevery/<int:did>',views.Assign,name="assign"),
    path('assignededlist/',views.AsignedList,name="assigendlist"),
    path('sntfeedback/',views.FEED,name="sntfeedback"),
    path('sntacomplaint/',views.COMP,name="sntcomplaint"),
    path('logout/',views.logout,name="logout"),
    path('gallery/<int:did>',views.Gallery,name="gallery"),
]