# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import Event

def index(request):
    context = {}
    return render(request, 'index.html', context)

def aboutUs(request):
    context = {}
    return render(request, 'aboutUs.html', context)

def aboutIEEE(request):
    context = {}
    return render(request, 'aboutIEEE.html', context)

def events(request):
    eventList = Event.objects.order_by('-create_date')
    futureEvents = Event.objects.filter(create_date__gte=timezone.now())
    pastEvents = Event.objects.filter(create_date__lt=timezone.now())
    context = {'eventList': eventList, 'futureEvents': futureEvents, 'pastEvents' : pastEvents}
    return render(request, 'events.html', context)

def specificEvent(request, event_id, slug):
    eventData = get_object_or_404(Event, pk=event_id)
    context = {'eventData':eventData}
    return render(request, 'specificEvent.html', context)
