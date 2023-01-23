from django.shortcuts import render
from app.models import *
from django.http import HttpResponse
# Create your views here.

def insert_topic(request):
    tn=input('Enter topic name')
    T=Topic.objects.get_or_create(topic_name=tn)[0]
    T.save()
    return HttpResponse('Topic is inserterd successfully')

def insert_webpage(request):
    tn=input('Enter topic_name')
    name=input('Enter name')
    url=input('Enter url')
    T=Topic.objects.get_or_create(topic_name=tn)[0]
    T.save()
    W=Webpage.objects.get_or_create(topic_name=T,name=name,url=url)[0]
    W.save()
    return HttpResponse('Topic is inserterd successfully')

def insert_acessrecord(request):
    tn=input('Enter topic_name')
    name=input('Enter name')
    url=input('Enter url')
    date=input('Enter date')
    T=Topic.objects.get_or_create(topic_name=tn)[0]
    T.save()
    W=Webpage.objects.get_or_create(topic_name=T,name=name,url=url)[0]
    W.save()
    A=AcessRecord.objects.get_or_create(name=W,date=date)[0]
    A.save()
    return HttpResponse('Topic is inserted successfully')
    