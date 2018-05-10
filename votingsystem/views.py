from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render_to_response
from django.contrib.auth.forms import UserCreationForm


def home(request):
    if request.method == 'POST':
        user = UserCreationForm(request.POST)
        if user.is_valid():
            user.save()
            return HttpResponseRedirect('login')
    return render(request, 'home.html', {'form': UserCreationForm})


@login_required()
def login_home(request):
    return render(request, 'login_home.html')
