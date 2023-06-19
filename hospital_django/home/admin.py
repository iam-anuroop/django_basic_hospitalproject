from django.contrib import admin
from .models import Department,Doctor,Booking

# Register your models here.
class DepartmentaAdmin(admin.ModelAdmin):
    list_display=('id','name','disp','fees')
admin.site.register(Department,DepartmentaAdmin)

admin.site.register(Doctor)

class BookingAdmin(admin.ModelAdmin):
    list_display=('id','p_name','s_date','p_email','d_name',"b_date")
admin.site.register(Booking,BookingAdmin)