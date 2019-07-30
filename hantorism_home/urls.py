from django.urls import path
from . import views

urlpatterns = [
    path('', views.list, name='list'),
    path('join/',views.join, name='join'),
    path('who/',views.who,name='who'),
    path('who/<str:ID>/',views.who_detail,name='who-id'),
]