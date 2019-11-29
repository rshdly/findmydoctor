from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from .models import Doctor, Appointment
from django.contrib.auth.hashers import make_password
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

# Create your views here.
def doctor_registration_view(request):
    if request.method == 'POST':
        user = User()
        user.first_name = request.POST['firstname']
        user.last_name = request.POST['lastname']
        user.username = request.POST['email']
        user.email = request.POST['email']
        user.password = make_password(request.POST['password'])
        user.save()
        doctor = Doctor()
        doctor.name = user.first_name + " " + user.last_name
        doctor.phone = request.POST['phone']
        doctor.email = request.POST['email']
        doctor.speciality = request.POST['speciality']
        doctor.qualification = request.POST['qualification']
        doctor.experience = request.POST['experience']
        doctor.fee = request.POST['fee']
        doctor.state = request.POST['state']
        doctor.city = request.POST['city']
        doctor.address = request.POST['address']
        doctor.photo = request.FILES['photo']
        doctor.weekdays = request.POST['weekdays']
        doctor.weekends = request.POST['weekends']
        doctor.weekdays_shift1_from = request.POST['weekdays_shift1_from']
        doctor.weekdays_shift1_to = request.POST['weekdays_shift1_to']
        doctor.weekdays_shift2_from = request.POST['weekdays_shift2_from']
        doctor.weekdays_shift2_to = request.POST['weekdays_shift2_to']
        doctor.weekends_shift1_from = request.POST['weekends_shift1_from']
        doctor.weekends_shift1_to = request.POST['weekends_shift1_to']
        doctor.weekends_shift2_from = request.POST['weekends_shift2_from']
        doctor.weekends_shift2_to = request.POST['weekends_shift2_to']
        doctor.save()
        return redirect('doctorlogin')
    return render(request, 'DoctorRegistration.html')

def doctor_login_view(request):
    if request.method == 'POST':
        user = authenticate(
            username = request.POST['email'],
            password = request.POST['password']
        )
        if user is not None:
            login(request, user)
            return redirect('appointments')
        else:
            return render(request, 'DoctorLogin.html')
    return render(request, 'DoctorLogin.html')

@login_required(login_url='doctorlogin')
def doctor_appointments_view(request):
    return render(request, 'Appointments.html', {'appointments': Appointment.objects.filter(doctor_email = request.user.email)})

@login_required(login_url='doctorlogin')
def doctor_profile_view(request):
    if request.method == 'POST':
        user = User.objects.get(id = request.user.id)
        user.first_name = request.POST['firstname']
        user.last_name = request.POST['lastname']
        user.username = request.POST['email']
        user.email = request.POST['email']
        user.save()
        doctor = Doctor.objects.get(user_id = request.user.id)
        doctor.phone = request.POST['phone']
        doctor.speciality = request.POST['speciality']
        doctor.qualification = request.POST['qualification']
        doctor.experience = request.POST['experience']
        doctor.fee = request.POST['fee']
        doctor.state = request.POST['state']
        doctor.city = request.POST['city']
        doctor.address = request.POST['address']
        doctor.photo = request.FILES['photo']
        doctor.weekdays = request.POST['weekdays']
        doctor.weekends = request.POST['weekends']
        doctor.weekdays_shift1_from = request.POST['weekdays_shift1_from']
        doctor.weekdays_shift1_to = request.POST['weekdays_shift1_to']
        doctor.weekdays_shift2_from = request.POST['weekdays_shift2_from']
        doctor.weekdays_shift2_to = request.POST['weekdays_shift2_to']
        doctor.weekends_shift1_from = request.POST['weekends_shift1_from']
        doctor.weekends_shift1_to = request.POST['weekends_shift1_to']
        doctor.weekends_shift2_from = request.POST['weekends_shift2_from']
        doctor.weekends_shift2_to = request.POST['weekends_shift2_to']
        doctor.save()
    return render(request, 'DoctorProfile.html', {'user': request.user})

@login_required(login_url='doctorlogin')
def doctor_change_password_view(request):
    if request.method == 'POST':
        user = User.objects.get(id = request.user.id)
        user.password = make_password(request.POST['newpassword'])
        user.save()
    return render(request, 'DoctorChangePassword.html')

@login_required(login_url='doctorlogin')
def doctor_logout_view(request):
    logout(request)
    return redirect('doctorlogin')