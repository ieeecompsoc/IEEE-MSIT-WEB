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
    futureEvents = Event.objects.filter(event_date__gte=timezone.now())
    pastEvents = Event.objects.filter(event_date__lt=timezone.now())
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
    mainMembers = Execom.objects.filter(chapter__chapter__contains="Main").order_by('-create_date')
    csMembers = Execom.objects.filter(chapter__chapter__contains="CS").order_by('-create_date')
    rasMembers = Execom.objects.filter(chapter__chapter__contains="RAS").order_by('-create_date')
    pesMembers = Execom.objects.filter(chapter__chapter__contains="PES").order_by('-create_date')
    wieMembers = Execom.objects.filter(chapter__chapter__contains="WIE").order_by('-create_date')
    taMembers = Execom.objects.filter(chapter__chapter__contains="TA").order_by('-create_date')
    context = {'allMembers':allMembers,'csMembers':csMembers,'rasMembers':rasMembers,'pesMembers':pesMembers,'wieMembers':wieMembers,'mainMembers':mainMembers,'taMembers':taMembers}
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

def cs(request):
    csMembers = Execom.objects.filter(chapter__chapter__contains="CS").order_by('-create_date')
    descriptions = Chapter.objects.filter()
    context = {'members':csMembers}
    return render(request,'cs.html',context)

def pes(request):
    pesMembers = Execom.objects.filter(chapter__chapter__contains="PES").order_by('-create_date')
    context = {'members':pesMembers}
    return render(request,'pes.html',context)

def ras(request):
    rasMembers = Execom.objects.filter(chapter__chapter__contains="RAS").order_by('-create_date')
    context = {'members':rasMembers}
    return render(request,'ras.html',context)

def wie(request):
    wieMembers = Execom.objects.filter(chapter__chapter__contains="WIE").order_by('-create_date')
    context = {'members':wieMembers}
    return render(request,'wie.html',context)