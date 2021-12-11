from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.forms import inlineformset_factory
from django.contrib.auth.forms import UserCreationForm
from .forms import *
from .models import *
from django.contrib import messages

def home(request):
    return render(request, 'main/index.html')


# def listofevents(request):
#     Event = newEVENT.objects.all()
#     return render(request, 'main/listofevents.html', {'Event': Event})
