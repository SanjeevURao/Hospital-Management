from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
import datetime



class Person(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    type = models.IntegerField(default=0)

    def __str__(self):
        return self.user.username

class Doctor(models.Model):
    person = models.OneToOneField(Person, on_delete=models.CASCADE)
    Speciality = models.CharField(max_length=100 , default=None)
    Address = models.CharField(max_length=100 , default=None)
    Email = models.CharField(max_length=100 , default=None)
    Phone = models.CharField(max_length=100 , default=None)
    gender = models.CharField(max_length=100 , default=None)

    def __str__(self):
        return self.person.user.username



class Receptionist(models.Model):
    person = models.OneToOneField(Person, on_delete=models.CASCADE)
    Address = models.CharField(max_length=100 , default=None)
    Email = models.CharField(max_length=100 , default=None)
    Phone = models.CharField(max_length=100 , default=None)
    gender = models.CharField(max_length=100 , default=None)

    def __str__(self):
        return self.person.user.username

class Patient(models.Model):
    person = models.OneToOneField(Person, on_delete=models.CASCADE)
    location = models.CharField(max_length=500 , blank=True , default='')
    bio = models.CharField(max_length=500, blank=True)
    Address = models.CharField(max_length=100 , default=None)
    Email = models.CharField(max_length=100 , default=None)
    Phone = models.CharField(max_length=100 , default=None)
    gender = models.CharField(max_length=100 , default=None)

    def __str__(self):
        return self.person.user.username


class Appointment(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE, null=True)
    Doctor = models.ForeignKey(Doctor , on_delete=models.CASCADE,default=None)
    Date = models.DateField(("Date"), default=datetime.date.today)
    Pending= 'PD'
    Approved= 'AP'
    Rejected = 'RJ'
    STATUS = (
        (Pending, 'Pending'),
        (Approved, 'Approved'),
        (Rejected, 'rejected'),
    )

    status = models.CharField(
        max_length=2,
        choices=STATUS,
        default=Pending,
    )

    message = models.CharField(max_length=1000 , default="Pending Approval")

    def __str__(self):
        return str(self.user)

    def get_absolute_url(self):
        return reverse('home:index')