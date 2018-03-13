from django.contrib.auth.models import User

from django import forms
from .models import  Appointment , Patient , Person, Doctor, Receptionist


class UserForm(forms.ModelForm):

    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'password']


class PersonForm(forms.ModelForm):

    class Meta:
        model = Person
        fields = ('type',)


class PatientForm(forms.ModelForm):
    class Meta:
        model = Patient
        fields = ('Address', 'Email', 'Phone', 'gender', 'location', 'bio')


class DoctorForm(forms.ModelForm):
    class Meta:
        model = Doctor
        fields = ('Address', 'Email', 'Phone', 'gender', 'Speciality',)


class ReceptionistForm(forms.ModelForm):
    class Meta:
        model = Receptionist
        fields = ('Address', 'Email', 'Phone', 'gender',)


class AppointmentForm(forms.ModelForm):

    class Meta:
        model = Appointment
        fields = ['Doctor', 'Date']


class Login(forms.ModelForm):

    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'password']


class UpdateForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ('username',)


