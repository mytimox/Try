from django.conf.urls import url, include
from django.contrib import admin
from . import views

#app_name = 'lalka'
urlpatterns =[
    #url(r'^landing/', views.landing, name='landing'),
    url(r'^basket_adding/$', views.basket_adding, name='basket_adding'),
]