from django.shortcuts import render
from django.http import HttpResponse


def welcome(request):
    return HttpResponse('Open API, App is Running')


def check_version(request):
    return render(request, 'version.html')


def send_name_object(request):
    return render(request, 'list.html', {'name' : 'Manuka'})