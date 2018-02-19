from django.db import models
from django.core.urlresolvers import reverse
from django.contrib.auth.models import  User
import datetime


class Doctor(models.Model):
    Name = models.CharField(max_length=100)
    Phone = models.CharField(max_length=15)
    Email = models.CharField(max_length=100)
    Speciality = models.CharField(max_length=100)

    def __str__(self):
        return self.Name

class Appointment(models.Model):
    user = models.ForeignKey(User, null=True)
    Doctor = models.ForeignKey(Doctor)
    Date = models.DateField(("Date"), default=datetime.date.today)

    def __str__(self):
        return str(self.user)

    def get_absolute_url(self):
        return reverse('home:index')