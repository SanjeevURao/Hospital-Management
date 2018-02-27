from django.db import models
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User
import datetime



class Person(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    is_doctor = models.BooleanField(default=True)

    def __str__(self):
        return self.user.username


class Doctor(models.Model):
    person = models.OneToOneField(Person, on_delete=models.CASCADE)
    Speciality = models.CharField(max_length=100 , default=None)

    def __str__(self):
        return self.person.user.username


class Patient(models.Model):
    person = models.OneToOneField(Person, on_delete=models.CASCADE)
    location = models.CharField(max_length=500 , blank=True , default='')
    bio = models.CharField(max_length=500, blank=True)

    def __str__(self):
        return self.person.user.username


class Appointment(models.Model):
    user = models.ForeignKey(User, null=True)
    Doctor = models.ForeignKey(Doctor , default=None)
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