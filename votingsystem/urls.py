
from django.urls import path, include
from .views import login_home, edit_profile, edit_password

urlpatterns = [
    path('home', login_home),
    path('edit', edit_profile),
    path('edit-password', edit_password)
]
