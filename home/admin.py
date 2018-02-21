from django.contrib import admin
from .models import  Doctor , Appointment , Person


admin.site.register(Doctor)
admin.site.register(Appointment)
admin.site.register(Person)

