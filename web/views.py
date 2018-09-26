# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import Event,Execom,Chapter,Designation,Achievment,Sig,Update

def index(request):
    news = Update.objects.order_by('-create_date')[:5]
    context = {'allNews': news}
    return render(request, 'index.html', context)

def aboutUs(request):
    context = {}
    return render(request, 'aboutUs.html', context)

def aboutIEEE(request):
    context = {}
    return render(request, 'aboutIEEE.html', context)

def events(request):
    eventList = Event.objects.order_by('-event_date')
    futureEvents = Event.objects.filter(event_date__gte=timezone.now())
    pastEvents = Event.objects.filter(event_date__lt=timezone.now())
    context = {'eventList': eventList, 'futureEvents': futureEvents, 'pastEvents' : pastEvents}
    return render(request, 'events.html', context)

def specificEvent(request, event_id, slug):
    eventData = get_object_or_404(Event, pk=event_id)
    context = {'eventData':eventData}
    return render(request, 'specificEvent.html', context)

def execom(request):
    allMembers = Execom.objects.all()
    #the below filter goes to Execom - Chapter from there it goes to Chapter - chapter where it finally searches the string.
    mainMembers = Execom.objects.filter(chapter__chapter__contains="Main")
    csMembers = Execom.objects.filter(chapter__chapter__contains="CS")
    mttsMembers = Execom.objects.filter(chapter__chapter__contains="MTTS")
    pesMembers = Execom.objects.filter(chapter__chapter__contains="PES")
    wieMembers = Execom.objects.filter(chapter__chapter__contains="WIE")
    taMembers = Execom.objects.filter(chapter__chapter__contains="TA")
    context = {'allMembers':allMembers,'csMembers':csMembers,'mttsMembers':mttsMembers,'pesMembers':pesMembers,'wieMembers':wieMembers,'mainMembers':mainMembers,'taMembers':taMembers}
    return render(request, 'execom.html', context)

def achievment(request):
    achievments = Achievment.objects.all()
    context = {'achievments':achievments}
    return render(request, 'achievment.html',context)

def sig(request):
    sig = Sig.objects.all()
    context={'sig':sig}
    return render(request,'sig.html',context)

def health(request):
    context={}
    return render(request,'health.html',context)
