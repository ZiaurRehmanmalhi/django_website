from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return render(request, 'index.html')


def removepunc(request):
    return HttpResponse("remove punc")


def capitalizefirst(request):
    return HttpResponse("capitalize first")


def newlineremove(request):
    return HttpResponse("newlineremove")


def spaceremove(request):
    return HttpResponse("spaceremove")


def charcount(request):
    return HttpResponse("charcount")