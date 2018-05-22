from django import forms
from .models import ToDo, Folder
from django.forms import ModelForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, UserChangeForm


class CreateProfileForm(UserCreationForm):

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name',
                  'password1', 'password2')
        help_texts = {'username': None, 'password1': None, 'password2': None}

    def save(self, commit=True):
        user = super(CreateProfileForm, self).save(commit=False)
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']

        if commit:
            user.save()
        return user


class EditProfileForm(UserChangeForm):

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password')


class FolderForm(ModelForm):

    class Meta:
        model = Folder
        fields = ('name', 'description')


class AddToDoForm(ModelForm):

    class Meta:
        model = ToDo
        fields = ('name', 'note')
