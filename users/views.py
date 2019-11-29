from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from doctors.models import Doctor, Appointment
from django.contrib.auth.hashers import make_password
from django.contrib.auth import authenticate, login, logout
from django.db.models import Q
from django.contrib.auth.decorators import login_required

# Create your views here.
def home_view(request):
    return render(request, 'SearchDoctor.html')

def search_doctors_view(request):
    return render(request, 'SearchResults.html',
    {'doctors': Doctor.objects.filter(
        Q(speciality=request.POST['speciality'])&
        Q(city=request.POST['city'])
    )})

def registration_view(request):
    if request.method == 'POST':
        user = User()
        user.first_name = request.POST['firstname']
        user.last_name = request.POST['lastname']
        user.email = request.POST['email']
        user.username = request.POST['email']
        user.password = make_password(request.POST['password'])
        user.save()
        return redirect('login')
    return render(request, 'UserRegistration.html')

def login_view(request):
    if request.method == 'POST':
        user = authenticate(
            username = request.POST['email'],
            password = request.POST['password']
        )
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            return render(request, 'UserLogin.html')
    return render(request, 'UserLogin.html')

@login_required(login_url='login')
def confirm_appointment_view(request):
    appointment = Appointment()
    appointment.appointment_date = request.POST['date']
    appointment.appointment_time = request.POST['time']
    appointment.name = request.POST['name']
    appointment.email = request.POST['email']
    appointment.phone = request.POST['phone']
    appointment.doctor_email = request.POST['doctoremail']
    appointment.save()
    return redirect('home')

@login_required(login_url='login')
def book_appointment_view(request):
    return render(request, 'BookAppointment.html', {'doctor': Doctor.objects.get(id=request.POST['doctorid'])})

@login_required(login_url='login')
def profile_view(request):
    if request.method == 'POST':
        user = User.objects.get(id = request.user.id)
        user.first_name = request.POST['firstname']
        user.last_name = request.POST['lastname']
        user.email = request.POST['email']
        user.username = request.POST['email']
        user.save()
    return render(request, 'UserProfile.html', {'user':request.user})

@login_required(login_url='login')
def change_password_view(request):
    if request.method == 'POST':
        user = User.objects.get(id = request.user.id)
        user.password = make_password(request.POST['newpassword'])
        user.save()
    return render(request, 'UserChangePassword.html')

@login_required(login_url='login')
def logout_view(request):
    logout(request)
    return redirect('login')

