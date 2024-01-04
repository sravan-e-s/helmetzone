from django.urls import path
from Deleveryboy import views
app_name="delevery"
urlpatterns = [
    path('dhome/',views.DeleveyBoy,name="dhome"),
    path('dprofile/',views.DProfile,name="dprofile"),
    path('editdboy/<int:edid>',views.Editdboy,name="editdboy"),
    path('changepassdboy/<int:cdid>',views.Changepassdboy,name="changepassdboy"),
    path('assigned/',views.AsignedList,name="assignlist"),
    path('completed/',views.CompletedList,name="completed"),
    path('complete/<int:cid>',views.completebook,name="completebook"),
    path('logout/',views.logout,name="logout"),

]