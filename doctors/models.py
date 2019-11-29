from django.db import models

# Create your models here.
class Doctor(models.Model):
    name = models.CharField(max_length=50,default=None)
    phone = models.CharField(max_length=15,default=None)
    email = models.CharField(max_length=15, default=None, blank=True)
    speciality = models.CharField(max_length=50,default=None)
    qualification = models.CharField(max_length=50,default=None)
    experience = models.IntegerField(default=0)
    fee = models.IntegerField(default=0)
    state = models.CharField(max_length=50,default=None)
    city = models.CharField(max_length=50,default=None)
    address = models.CharField(max_length=100,default=None)
    photo = models.ImageField(upload_to='doctors_pics',default='default.png')
    weekdays = models.CharField(max_length=100,default=None)
    weekends = models.CharField(max_length=100,default=None)
    weekdays_shift1_from = models.CharField(max_length=50,default=None)
    weekdays_shift1_to = models.CharField(max_length=50,default=None)
    weekdays_shift2_from = models.CharField(max_length=50, default=None)
    weekdays_shift2_to = models.CharField(max_length=50, default=None)
    weekends_shift1_from = models.CharField(max_length=50, default=None)
    weekends_shift1_to = models.CharField(max_length=50, default=None)
    weekends_shift2_from = models.CharField(max_length=50, default=None)
    weekends_shift2_to = models.CharField(max_length=50, default=None)

    def __str__(self):
        return self.name

class Appointment(models.Model):
    appointment_date = models.CharField(max_length=50,default=None)
    appointment_time = models.CharField(max_length=50,default=None)
    name = models.CharField(max_length=50,default=None)
    email = models.CharField(max_length=50, default=None, blank=True)
    phone = models.CharField(max_length=15,default=None)
    doctor_email = models.CharField(max_length=50, default=None, blank=True)

    def __str__(self):
        return self.name
