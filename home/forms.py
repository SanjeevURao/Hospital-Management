from django.contrib.auth.models import User

from django import forms
from .models import  Appointment


class UserForm(forms.ModelForm):

    password = forms.CharField(widget=forms.PasswordInput)

    #this class is info abt the form
    class Meta:
        model = User

        fields = ['username' , 'email' , 'password']


class AppointmentForm(forms.ModelForm):

    #this class is info abt the form
    class Meta:
        model = Appointment

        fields = ['Doctor' , 'Date']

class Login(forms.ModelForm):

    password = forms.CharField(widget=forms.PasswordInput)

    #this class is info abt the form
    class Meta:
        model = User

        fields = ['username', 'password']


