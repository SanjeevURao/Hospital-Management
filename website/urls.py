from django.urls import path , include
from django.contrib import admin

urlpatterns = [
    path('', include(('home.urls','home'), namespace='home')),
    path('admin/', admin.site.urls),
    path('index/', include('home.urls')),
]

