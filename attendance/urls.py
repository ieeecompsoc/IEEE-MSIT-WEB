from django.urls import path
from attendance import views

urlpatterns = [
    path(r'',views.index,name='home'),
    path(r'/file',views.file,name='file'),
]