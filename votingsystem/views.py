from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import PasswordChangeForm
from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import CreateProfileForm, EditProfileForm, AddToDoForm
from django.contrib.auth import update_session_auth_hash
from .models import ToDo


def register(request):
    if request.method == 'POST':
        user = CreateProfileForm(request.POST)
        if user.is_valid():
            user.save()
            return HttpResponseRedirect('/login')
    return render(request, 'registration/register.html', {'form': CreateProfileForm})


def home(request):
    return render(request, 'home.html')


@login_required()
def login_home(request):
    original_form = AddToDoForm
    todos = ToDo.objects.filter(user=request.user.profile)
    if request.method == 'POST':
        form = AddToDoForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            note = form.cleaned_data['note']
            add = ToDo(user=request.user.profile, name=name,note=note)
            add.save()
            return HttpResponseRedirect('/account/home')

    return render(request, 'registration/login_home.html', {'form': original_form,
                                                            'todos': todos})


@login_required()
def edit_profile(request):
    if request.method == 'POST':
        form = EditProfileForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/account/home')
    else:
        form = EditProfileForm(instance=request.user)
        return render(request, 'registration/edit_profile.html', {'form': form})


@login_required()
def edit_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(data=request.POST, user=request.user)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            return HttpResponseRedirect('/account/home')
        else:
            return HttpResponseRedirect('/account/edit-password')
    else:
        form = PasswordChangeForm(request.user)
        return render(request, 'registration/edit_password.html', {'form': form})
