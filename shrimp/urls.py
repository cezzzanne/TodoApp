
from django.contrib import admin
from django.urls import path, include
from votingsystem.views import home, register
from django.contrib.auth.views import login

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home),
    path('register/', register),
    path('login', login),
    path('account/', include('votingsystem.urls'))

]
