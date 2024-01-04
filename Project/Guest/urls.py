from django.urls import path
from Guest import views
app_name="Guest"
urlpatterns = [
    path('news/',views.Newseller,name="Newseller.html"),
    path('newu/',views.Newuser,name="Newuser.html"),
    path('ajaxplace/',views.Ajaxplace,name="Ajax-place"),
    path('login/',views.Login,name="login"),
     path('viewproducts/',views.Viewproducts,name="vp"),
    path('',views.homepage,name="Home"),

]