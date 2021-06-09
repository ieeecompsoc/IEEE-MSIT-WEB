# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, get_object_or_404
from django.utils import timezone
# HttpResponse,HttpResponseRedirect,
from django.http import JsonResponse
import json
from django.views.decorators.csrf import csrf_exempt
from .models import Event,Execom,Chapter,Designation,Achievment,Sig,Update,Team,Blog

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

def blogs(request):
    blogList = Blog.objects.order_by('-blog_date')
    context = {'blogList': blogList}
    return render(request, 'blogs.html', context)

def specificBlog(request, blog_id, slug):
    blogData = get_object_or_404(Blog, pk=blog_id)
    context = {'blogData': blogData}
    return render(request, 'specificBlog.html', context)

def execom(request):
    allMembers = Execom.objects.all().order_by('page_rank','designation__designation') # Sorted for proper order in frontend
    #the below filter goes to Execom - Chapter from there it goes to Chapter - chapter where it finally searches the string.

#     mainMembers = []    #list containing queryset for all pageRanks for a chapter
#     mainMembersMaxRank = 3  #maximum pagerank for the chapter
#     for pageRank in range(1,mainMembersMaxRank+1):
#         mainMembers_ranked = Execom.objects.filter(chapter__chapter__contains="Main",page_rank=pageRank).order_by('page_rank','-create_date')
#         mainMembers.append(mainMembers_ranked)

#     csMembers = []
#     csMembersMaxRank = 5
#     for pageRank in range(1,csMembersMaxRank+1):
#         csMembers_ranked = Execom.objects.filter(chapter__chapter__contains="CS",page_rank=pageRank).order_by('page_rank','-create_date')
#         csMembers.append(csMembers_ranked)

#     rasMembers = []
#     rasMembersMaxRank = 5
#     for pageRank in range(1,rasMembersMaxRank+1):
#         rasMembers_ranked = Execom.objects.filter(chapter__chapter__contains="RAS",page_rank=pageRank).order_by('page_rank','-create_date')
#         rasMembers.append(rasMembers_ranked)

#     pesMembers = []
#     pesMembersMaxRank = 5
#     for pageRank in range(1,pesMembersMaxRank+1):
#         pesMembers_ranked = Execom.objects.filter(chapter__chapter__contains="PES",page_rank=pageRank).order_by('page_rank','-create_date')
#         pesMembers.append(pesMembers_ranked)

#     wieMembers = []
#     wieMembersMaxRank = 5
#     for pageRank in range(1,wieMembersMaxRank+1):
#         wieMembers_ranked = Execom.objects.filter(chapter__chapter__contains="WIE",page_rank=pageRank).order_by('page_rank','-create_date')
#         wieMembers.append(wieMembers_ranked)

#     taMembers = []
#     taMembersMaxRank = 5
#     for pageRank in range(1,wieMembersMaxRank+1):
#         taMembers_ranked = Execom.objects.filter(chapter__chapter__contains="TA",page_rank=pageRank).order_by('page_rank','-create_date')
#         taMembers.append(taMembers_ranked)


#   context = {'allMembers':allMembers,'csMembers':csMembers,'rasMembers':rasMembers,'pesMembers':pesMembers,'wieMembers':wieMembers,'mainMembers':mainMembers,'taMembers':taMembers}

    records = {} # To create context later
    # NEED SORTED LIST FOR THIS LOOP ASSUMING RANKS ARE CONTINOUS
    for member in allMembers: # To divide members and extract all chapters and committees
        currChapter = member.chapter.chapter
        if currChapter in records:
            index = int(member.page_rank)
            if len(records[currChapter])>=index:
                records[currChapter][index-1].append(member)
            else:
                records[currChapter].append([member])
        else:
            records[currChapter] = [[member]]
    print(records.keys())
    return render(request, 'execom.html', {'records':records})

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

def tpe(request):
    context={}
    return render(request,'tpe.html',context)

def team(request):
    team = Team.objects.all()
    context = {'team': team}
    return render(request, 'team.html', context)

def cs(request):
    csMembers = Execom.objects.filter(chapter__chapter__contains="CS").order_by('page_rank','-create_date')
    context = {'members':csMembers}
    return render(request,'cs.html',context)

def pes(request):
    pesMembers = Execom.objects.filter(chapter__chapter__contains="PES").order_by('page_rank','-create_date')
    context = {'members':pesMembers}
    return render(request,'pes.html',context)

def ras(request):
    rasMembers = Execom.objects.filter(chapter__chapter__contains="RAS").order_by('page_rank','-create_date')
    context = {'members':rasMembers}
    return render(request,'ras.html',context)

def wie(request):
    wieMembers = Execom.objects.filter(chapter__chapter__contains="WIE").order_by('page_rank','-create_date')
    context = {'members':wieMembers}
    return render(request,'wie.html',context)
