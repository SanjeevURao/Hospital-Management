from django.shortcuts import render , redirect
from django.contrib.auth import authenticate , login , logout
from django.views.generic import View
from .models import Appointment, Person , Doctor , User , Patient, Receptionist
from django.views.generic.edit import UpdateView , DeleteView
from .forms import UserForm , PatientForm , DoctorForm , PersonForm , UpdateForm, ReceptionistForm
from django.contrib.auth.decorators import login_required
from .forms import AppointmentForm
from django.core.urlresolvers import reverse_lazy
from django.shortcuts import redirect


def test(request):
    return render(request, 'home/test.html')


@login_required(login_url='login')
def index(request):
    users = User.objects.all()
    appointments = Appointment.objects.filter(user=request.user)
    return render(request, 'home/index.html', {'appointments': appointments , 'Users':users})


@login_required(login_url='login')
def doctor_list(request):
    doctors = Doctor.objects.all()
    return render(request, 'home/doctor_list.html', {'doctors': doctors})


@login_required(login_url='login')
def doctor_home(request):
    user = request.user
    person = Person.objects.get(user=user)
    doctor = Doctor.objects.get(person=person)
    appointments = Appointment.objects.filter(Doctor=doctor)
    return render(request, 'home/doctor_home.html', {'appointments': appointments})



@login_required(login_url='login')
def receptionist_home(request):
    user = request.user
    person = Person.objects.get(user=user)
    receptionist = Receptionist.objects.get(person=person)
    appointments = Appointment.objects.all()
    return render(request, 'home/receptionist_home.html', {'appointments': appointments})



@login_required(login_url='login')
def admin_home(request):
    return render(request, 'home/admin_home.html')


class UserFormView(View):

    user_form_class = UserForm
    patient_form_class = PatientForm
    template_name = 'home/registration.html'

    #show blank forqm

    def get(self , request):
        u_form = self.user_form_class(None)
        p_form = self.patient_form_class(None)
        return render(request , self.template_name , {'u_form' : u_form , 'p_form' : p_form})

    #register user

    def post(self , request):
        u_form = self.user_form_class(request.POST)
        p_form = self.patient_form_class(request.POST)
        if u_form.is_valid() and p_form.is_valid():

            #save user info locally and not in the database yet
            user = u_form.save(commit=False)
            patient = p_form.save(commit=False)

            #cleaned data
            username = u_form.cleaned_data['username']
            password = u_form.cleaned_data['password']

            #can not directly update password because it is stored  as a hash value
            user.set_password(password)
            user.save()

            person = Person(user=user)

            person.save()

            #save info to DB
            patient.person = Person.objects.get(user=user)
            patient.save()

            user = authenticate(username=username , password=password)

            if user is not None:
                if user.is_active:
                    login(request, user)
                return redirect('home:index')

        # if fails , then return form
        return render(request , self.template_name , {'u_form' : u_form , 'p_form' : p_form})


class DoctorFormView(View):

    user_form_class = UserForm
    doctor_form_class = DoctorForm
    person_form_class = PersonForm
    template_name = 'home/doctor_registration.html'

    #show blank forqm

    def get(self , request):
        u_form = self.user_form_class(None)
        p_form = self.person_form_class(None)
        d_form = self.doctor_form_class(None)
        return render(request , self.template_name , {'u_form' : u_form , 'p_form' : p_form,  'd_form' : d_form})

    #register user

    def post(self , request):
        u_form = self.user_form_class(request.POST)
        p_form = self.person_form_class(request.POST)
        d_form = self.doctor_form_class(request.POST)
        if u_form.is_valid() and d_form.is_valid() and p_form.is_valid():

            #save user info locally and not in the database yet
            user = u_form.save(commit=False)
            doctor = d_form.save(commit=False)
            person = p_form.save(commit=False)

            #cleaned data

            username = u_form.cleaned_data['username']
            password = u_form.cleaned_data['password']

            #can not directly update password because it is stored  as a hash value
            user.set_password(password)
            user.save()
            person.save()


            person = Person(user=user)
            person.save()


            #save info to DB
            doctor.person = Person.objects.get(user=user)
            doctor.save()
            return redirect('home:admin_home')

        # if fails , then return form
        return render(request , self.template_name , {'u_form' : u_form , 'd_form' : d_form})


class ReceptionistFormView(View):

    user_form_class = UserForm
    receptionist_form_class = ReceptionistForm
    person_form_class = PersonForm
    template_name = 'home/doctor_registration.html'

    #show blank forqm

    def get(self , request):
        u_form = self.user_form_class(None)
        p_form = self.person_form_class(None)
        d_form = self.receptionist_form_class(None)
        return render(request , self.template_name , {'u_form' : u_form , 'p_form' : p_form,  'd_form' : d_form})

    #register user

    def post(self , request):
        u_form = self.user_form_class(request.POST)
        p_form = self.person_form_class(request.POST)
        d_form = self.receptionist_form_class(request.POST)
        if u_form.is_valid() and d_form.is_valid() and p_form.is_valid():

            #save user info locally and not in the database yet
            user = u_form.save(commit=False)
            doctor = d_form.save(commit=False)
            person = p_form.save(commit=False)

            #cleaned data

            username = u_form.cleaned_data['username']
            password = u_form.cleaned_data['password']

            #can not directly update password because it is stored  as a hash value
            user.set_password(password)
            user.save()
            person.save()


            person = Person(user=user)
            person.save()


            #save info to DB
            doctor.person = Person.objects.get(user=user)
            doctor.save()
            return redirect('home:admin_home')

        # if fails , then return form
        return render(request , self.template_name , {'u_form' : u_form , 'd_form' : d_form})


@login_required(login_url='login')
def login_success(request):
    if request.user.is_superuser:
        return redirect("home:admin_home")
    person=Person.objects.get(user=request.user)
    if person.type == 1:
        return redirect("home:doctor_home")
    if person.type == 2:
        return redirect("home:receptionist_home")
    else:
        return redirect("home:index")


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

doctor_home
class UserUpdate(UpdateView):

    context_object_name = 'form'
    form_class = UpdateForm
    template_name = 'home/userupdate.html'
    success_url = 'success'

    # get object
    def get_object(self, queryset=None):
        return self.request.user

    # override form_valid method
    def form_valid(self, form):
        # save cleaned post data
        clean = form.cleaned_data
        self.object = form.save(clean)
        return super(UserUpdate, self).form_valid(form)

def Success(request):
    return render(request, 'home/success.html')


def all_appointments(request):
    appointments = Appointment.objects.all()
    return render(request, 'home/all_appointments.html', {'appointments': appointments})