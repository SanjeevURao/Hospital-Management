from django.urls import path
from . import views
from django.contrib.auth.views import LoginView , LogoutView
from .views import UserUpdate , Success


urlpatterns = [
    path('', views.index , name='index'),
    path('login_success/', views.login_success, name='login_success'),
    path('test/', views.test, name='test'),
    path('doctor_list/', views.doctor_list, name='doctor_list'),
    path('doctor_home', views.doctor_home, name='doctor_home'),
    path('receptionist_home', views.receptionist_home, name='receptionist_home'),
    path('admin_home', views.admin_home, name='admin_home'),
    path('all_appointments', views.all_appointments, name='all_appointments'),
    path('register', views.UserFormView.as_view() , name='register'),
    path('doctor_register', views.DoctorFormView.as_view(), name='doctor_register'),
    path('receptionist_register', views.ReceptionistFormView.as_view(), name='receptionist_register'),
    path('login/',LoginView.as_view(template_name="home/login.html"), {'template_name': 'home/login.html'} ,name='login'),
    path('appointment/add', views.AddAppointment, name='addappointment'),
    path('appointment/<int:pk>/delete/', views.AppointmentDelete.as_view(), name='deleteappointment'),
    path('appointment/<int:pk>/', views.AppointmentUpdate.as_view(), name='updateappointment'),
    path('profile/edit/',UserUpdate.as_view(),name='user-update'),
    path('profile/edit/success', Success, name='success'),
    path('logout/',LogoutView.as_view(), {'next_page': '/index/login'}, name='logout'),
]