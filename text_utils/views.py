# http://127.0.0.1:8000/
from django.http import HttpResponse
from django.shortcuts import render
from django.shortcuts import redirect


def index(request):
    return render(request, 'index2.html')


def removepunc(request):
    djtext = djtext = request.POST.get('text', 'default')
    removepunc = request.POST.get('removepunc', 'off')
    if removepunc == "on":
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        analyzed = ""
        for char in djtext:
            if char not in punctuations:
                analyzed = analyzed + char
        params = {'purpose': 'Removed Punctuations', 'analyzed_text': analyzed}
        djtext = analyzed
    return HttpResponse("removepunc")


def tictac(request):
    # return HttpResponse('our services')
    return render(request, 'game.html')


def portfolio(request):
    return redirect('https://www.ziamalhi.com/')


def spaceremove(request):
    return HttpResponse("space remove")


def contact(request):
    return HttpResponse("contact")


def speach(request):
    return render(request, 'text_to_speach.html')
