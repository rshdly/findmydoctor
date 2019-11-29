"""findmydoctor URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from django.conf import settings
from django.conf.urls.static import static
from users import views as users_views
from doctors import views as doctors_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('doctorregistration/', doctors_views.doctor_registration_view, name = 'doctorregistration'),
    path('doctorlogin/', doctors_views.doctor_login_view, name = 'doctorlogin'),
    path('appointments/', doctors_views.doctor_appointments_view, name = 'appointments'),
    path('doctorprofile/', doctors_views.doctor_profile_view, name = 'doctorprofile'),
    path('doctorchangepassword/', doctors_views.doctor_change_password_view, name = 'doctorchangepassword'),
    path('doctorlogout/', doctors_views.doctor_logout_view, name = 'doctorlogout'),
    path('searchdoctors/', users_views.search_doctors_view, name = 'searchdoctors'),
    path('register/', users_views.registration_view, name = 'register'),
    path('login/', users_views.login_view, name = 'login'),
    path('', users_views.home_view, name = 'home'),
    path('bookappointment/', users_views.book_appointment_view, name = 'bookappointment'),
    path('confirmappointment/', users_views.confirm_appointment_view, name = 'confirmappointment'),
    path('profile/', users_views.profile_view, name = 'profile'),
    path('changepassword/', users_views.change_password_view, name = 'changepassword'),
    path('logout/', users_views.logout_view, name = 'logout'),
]

urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
