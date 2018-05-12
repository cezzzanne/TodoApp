from django.contrib import admin
from .models import Profile, ToDo, Folder

# Register your models here.
admin.site.register(Profile)
admin.site.register(ToDo)
admin.site.register(Folder)
