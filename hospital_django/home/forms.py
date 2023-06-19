from django import forms
from .models import Booking
class Dateinput(forms.DateInput):
    input_type='date'

class Bookingform(forms.ModelForm):
    class Meta:
       model=Booking
       fields='__all__'
       widgets = {
           's_date': Dateinput()
       }

       labels = {
            'p_name':"patient name",
            'p_spec':"patient Address and phone",
            'p_email':"patient email",
            'd_name':"doctor name",
            's_date':"sheduled date",
            'b_date':"booked on"
       }