from django.urls import path
from . import views
urlpatterns= [
    path('home/',views.home , name="home"),
    path('',views.signuppage , name="signup"),
    path('login/',views.loginpage , name="login"),
    path('logout/',views.logoutpage,name="logout"),

]