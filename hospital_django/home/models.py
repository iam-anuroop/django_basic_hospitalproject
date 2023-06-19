from django.db import models

# Create your models here.
class Department(models.Model):
    name=models.CharField(max_length=100)
    disp=models.TextField(max_length=150)
    fees=models.IntegerField()

    def __str__(self):
        return self.name ,self.disp
    
class Doctor(models.Model):
    d_name=models.CharField(max_length=100)
    d_spec=models.TextField(max_length=150)
    d_disp=models.ForeignKey(Department,on_delete=models.CASCADE)
    d_img=models.ImageField(upload_to='doctorsimage')
    
    def __str__(self):
        return self.d_name +'('+ self.d_spec +')'
    

class Booking(models.Model):
    p_name=models.CharField(max_length=100)
    p_spec=models.TextField(max_length=150)
    p_email=models.EmailField()
    d_name=models.ForeignKey(Doctor,on_delete=models.CASCADE)
    s_date=models.DateField()
    b_date=models.DateField(auto_now=True)

    def __str__(self):
        return self.p_name