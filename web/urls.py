from django.urls import path
from . import views

urlpatterns = [
    path(r'', views.index, name='index'),
    path(r'aboutUs', views.aboutUs, name='aboutUs'),
    path(r'aboutIEEE', views.aboutIEEE, name='aboutIEEE'),
    path(r'events', views.events, name='events'),
    path(r'events/<int:event_id>/<slug:slug>', views.specificEvent, name='specificEvent'),
    path(r'ExCom', views.execom, name='execom'),
    path(r'achievments', views.achievment, name='achievment'),
    path(r'sig', views.sig, name='sig'),
    path(r'health', views.health, name='health'),
    path(r'tpe', views.tpe, name='tpe'),
]
