from django.db import models
from django.core.urlresolvers import reverse
from django.contrib.auth.models import  User
import datetime
from django.db.models.signals import post_save
from django.dispatch import receiver

class Person(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE , primary_key=True)
    bio = models.CharField(max_length=500, blank=True , default='')

    def __str__(self):
        return self.user.username

    @receiver(post_save, sender=User)
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            Person.objects.create(user=instance)


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


    def __str__(self):
        return str(self.user)

    def get_absolute_url(self):
        return reverse('home:index')

