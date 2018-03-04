from django.contrib.auth.models import User

from django import forms
from .models import  Appointment , Patient , Person, Doctor


class UserForm(forms.ModelForm):

    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'email', 'password']


class PersonForm(forms.ModelForm):

    class Meta:
        model = Person
        fields = ('is_doctor',)


class PatientForm(forms.ModelForm):
    class Meta:
        model = Patient
        fields = ('location', 'bio')


class DoctorForm(forms.ModelForm):
    class Meta:
        model = Doctor
        fields = ('Speciality',)


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


