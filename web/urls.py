from django.urls import path
from . import views

urlpatterns = [
    path(r'', views.index, name='index'),
    path(r'aboutUs', views.aboutUs, name='aboutUs'),
    path(r'aboutIEEE', views.aboutIEEE, name='aboutIEEE'),
    path(r'events', views.events, name='events'),
    path(r'events/<int:event_id>/<slug:slug>', views.specificEvent, name='specificEvent'),
    path(r'ExeCom', views.execom, name='execom'),
    path(r'achievments', views.achievment, name='achievment'),
    path(r'sig', views.sig, name='sig'),
    path(r'health', views.health, name='health'),
    path(r'spp2019', views.spp, name='spp'),
    path(r'team', views.team, name='team'),
    path(r'compsoc',views.cs,name='cs'),
    path(r'pes',views.pes,name="pes"),
    path(r'ras',views.ras,name="ras"),
    path(r'wie',views.wie,name="wie")
]
