from django.conf.urls import url , include
from . import views
from django.contrib import admin
from django.contrib.auth.views import login , logout

urlpatterns = [
    url(r'^$', views.index , name='index'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^register$' , views.UserFormView.as_view() , name='register'),
    url(r'^login/$',login, {'template_name': 'home/login.html'} ,name='login'),
    url(r'^appointment/add$', views.AddAppointment, name='addappointment'),
    url(r'^appointment/(?P<pk>[0-9]+)/delete/$', views.AppointmentDelete.as_view(), name='deleteappointment'),
    url(r'^appointment/(?P<pk>[0-9]+)/$', views.AppointmentUpdate.as_view(), name='updateappointment'),
    url(r'^logout/$',logout, {'next_page': '/'}, name='logout'),
]



