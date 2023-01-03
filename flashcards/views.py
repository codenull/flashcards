from django.shortcuts import render
from django.db.models import Count
from django.http import Http404, HttpResponse



def index(request):
    return HttpResponse('Это главная страница.')
