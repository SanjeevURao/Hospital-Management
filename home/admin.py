from django.contrib import admin
from .models import  Doctor , Appointment , Person , Patient, Receptionist

admin.site.register(Doctor)
admin.site.register(Appointment)
admin.site.register(Person)
admin.site.register(Patient)
admin.site.register(Receptionist)