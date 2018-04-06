from django.urls import path
from . import views

app_name = 'HanksBank3'
urlpatterns = [

    #path('hello/', views.hello, name='hello'),
    #path('time/', views.time, name='time'),
    #path('BMI/', views.BMI, name='BMI'),
    path('getLoan/', views.form, name='form'),
    path('decision/', views.decision, name='decision'),
    path("", views.menu, name='menu'),
    path('no/', views.no, name='no'),


]