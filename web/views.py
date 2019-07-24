# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import Event,Execom,Chapter,Designation,Achievment,Sig,Update,Team

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
    futureEvents = Event.objects.filter(event_date__gte=timezone.now()).order_by('-event_date')
    pastEvents = Event.objects.filter(event_date__lt=timezone.now()).order_by('-event_date')
    context = {'eventList': eventList, 'futureEvents': futureEvents, 'pastEvents' : pastEvents}
    return render(request, 'events.html', context)

def specificEvent(request, event_id, slug):
    eventData = get_object_or_404(Event, pk=event_id)
    futureEvents = Event.objects.filter(event_date__gte=timezone.now())
    pastEvents = Event.objects.filter(event_date__lt=timezone.now())
    context = {'eventData':eventData, 'futureEvents': futureEvents, 'pastEvents' : pastEvents}
    return render(request, 'specificEvent.html', context)

def execom(request):
    allMembers = Execom.objects.all()
    #the below filter goes to Execom - Chapter from there it goes to Chapter - chapter where it finally searches the string.
    mainMembers = Execom.objects.filter(chapter__chapter__contains="Main").order_by('order')
    csMembers = Execom.objects.filter(chapter__chapter__contains="CS").order_by('order')
    mttsMembers = Execom.objects.filter(chapter__chapter__contains="MTTS").order_by('order')
    pesMembers = Execom.objects.filter(chapter__chapter__contains="PES").order_by('order')
    wieMembers = Execom.objects.filter(chapter__chapter__contains="WIE").order_by('order')
    taMembers = Execom.objects.filter(chapter__chapter__contains="TA").order_by('order')
    rasMembers = Execom.objects.filter(chapter__chapter__contains="RAS").order_by('order')
    context = {'allMembers':allMembers,'csMembers':csMembers,'mttsMembers':mttsMembers,'pesMembers':pesMembers,'wieMembers':wieMembers,'mainMembers':mainMembers,'taMembers':taMembers, 'rasMembers':rasMembers}
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

def spp(request):
    context = {}
    return render(request, 'spp2019.html', context)
    
def team(request):
	team = Team.objects.all()
	context = {'team': team}
	return render(request, 'team.html', context)
