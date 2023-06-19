from django.shortcuts import render
from .models import Department,Doctor
from .forms import Bookingform
# Create your views here.

def index(request):
    anuroop={
           'f':['apple','orange','grapes']
    }
    return render(request,"index.html",anuroop)

def about(request):
    return render(request,"about.html")

def Booking(request):
        if request.method=='POST':
               form=Bookingform(request.POST)
               if form.is_valid():
                      form.save()
                      return render(request,'Confirmation.html')
        form = Bookingform()
        d_form={
               'form':form
        }
        return render(request,"booking.html",d_form)

def Doctors(request):
        print(request)
        doct={
               'doc':Doctor.objects.all()
        }
        return render(request,"doctors.html",doct)

def Contact(request):
        return render(request,"contact.html")

def department(request):
        dip={
               'd':Department.objects.all()
        }
        return render(request,"Department.html",dip)