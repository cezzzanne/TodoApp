from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    name = models.CharField(max_length=50, null=True)
    last_name = models.CharField(max_length=50, null=True)
    image = models.ImageField(upload_to='profile_pictures', blank=True)

    def __str__(self):
        return self.user.username


def create_profile(sender, **kwargs):
    if kwargs['created']:
        Profile.objects.create(user=kwargs['instance'])


post_save.connect(create_profile, sender=User)


class Folder(models.Model):
    user = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='folder')
    name = models.CharField(max_length=200, default="")
    description = models.CharField(max_length=300, null=True, blank=True)

    def __str__(self):
        return self.name


class ToDo(models.Model):
    folder = models.ForeignKey(Folder, on_delete=models.CASCADE, related_name='todo', default='')
    name = models.CharField(max_length=100)
    note = models.CharField(max_length=700)

    def __str__(self):
        return self.name
