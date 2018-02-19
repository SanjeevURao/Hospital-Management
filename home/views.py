from django.template import loader
from django.shortcuts import render , redirect
from django.contrib.auth import authenticate , login
from django.views.generic import View
from .models import Appointment
from django.views.generic.edit import CreateView , UpdateView , DeleteView
from .forms import UserForm
from django.contrib.auth.decorators import login_required
from .forms import AppointmentForm
from django.core.urlresolvers import reverse_lazy

@login_required(login_url='login')
def index(request):
    template = loader.get_template('home/index.html')
    appointments = Appointment.objects.filter(user=request.user)
    return render(request, 'home/index.html', {'appointments': appointments})


class UserFormView(View):
    form_class = UserForm
    template_name = 'home/registration.html'
    #show blank form
    def get(self , request):
        form = self.form_class(None)
        return render(request , self.template_name , {'form' : form})

    #register user
    def post(self , request):
        form = self.form_class(request.POST)

        if form.is_valid():

            #save user info locally and not in the database yet

            user = form.save(commit=False)

            #cleaned data

            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            #can not directly update password because it is stored  as a hash value

            user.set_password(password)

            #save info to DB

            user.save()

            user = authenticate(username=username , password=password)

            if user is not None:

                if user.is_active:

                   login(request, user)

                   return redirect('home:index')

        # if fails , then return form

        return render(request , self.template_name , {'form' : form})


@login_required(login_url='login')
def AddAppointment(request):
    if not request.user.is_authenticated():
        return render(request, 'index/login.html')
    else:
        form = AppointmentForm(request.POST or None)
        if form.is_valid():
            appointment = form.save(commit=False)
            appointment.user = request.user

            appointment.save()
            appointments = Appointment.objects.filter(user=request.user)
            return render(request, 'home/index.html', {'appointments': appointments})
        context = {
                "form": form,
            }
    return render(request, 'home/appointment_form.html', context)


class AppointmentDelete(DeleteView):
    model = Appointment
    success_url = reverse_lazy('home:index')

class AppointmentUpdate(UpdateView):
    model = Appointment
    fields = ['Name']









