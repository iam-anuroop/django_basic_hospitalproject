from django.urls import path
from . import views



urlpatterns = [
    path('',views.index,name="home"),
    path('about', views.about,name="about"),
    path('doctors', views.Doctors,name="doctors"),
    path('booking', views.Booking,name="booking"),
    path('contact', views.Contact,name="contact"),
    path('department', views.department,name="department"),
]  