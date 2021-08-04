"""urlshortner URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from urlshortner.views import dashboard, event, generate_url,remove_url,edit_url
from django.conf.urls import url
from django.contrib.auth import views as auth_views


urlpatterns = [
    path(r'', dashboard, name='dashboard'),
    path(r'generate/', generate_url, name='generate_url'),
    path(r'<str:query>/', event, name='event'),
    url(r'^delete/(?P<u_id>[0-9]+)/$', remove_url, name='remove_url'),
    path('edit/<u_id>', edit_url, name='edit_url'),
    path('login', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout', auth_views.LogoutView.as_view(template_name='logout.html'), name='logout')
]
