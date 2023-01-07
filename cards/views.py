from django.shortcuts import render
from django.db.models import Count
from django.http import Http404, HttpResponse


def index(request):
    return render(request, 'index.html')
    # return HttpResponse('Это главная страница.')

def registration(request):
    return render(request, 'registration.html')
