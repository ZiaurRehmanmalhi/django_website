# http://127.0.0.1:8000/
from django.http import HttpResponse
from django.shortcuts import render
from django.shortcuts import redirect


def index(request):
    return render(request, 'index.html')


def analize(request):
    global analized
    djtext = request.GET.get('text', 'default')
    removepunc = request.GET.get('removepunc', 'off')
    fullcaps = request.GET.get('fullcaps', 'off')

    if removepunc == "on":
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        analized = ""
        for char in djtext:
            if char not in punctuations:
                analized = analized + char
        params = {'purpose': 'Remove punctuation', 'analized_text': analized}
        return render(request, 'analize.html', params)

    elif(fullcaps=="on"):
        analize = ""
        for char in djtext:
            analized = analized + char.upper()
        params = {'purpose': 'change to uppercase', 'analized_text': analized}
        return render(request, 'analize.html', params)
    else:
        return HttpResponse('Error')


def newlineremover(request):
    return HttpResponse("newlineremover")


def spaceremove(request):
    return HttpResponse("space remove")


def tictac(request):
    # return HttpResponse('our services')
    return render(request, 'game.html')


def portfolio(request):
    return redirect('https://www.ziamalhi.com/')


def contact(request):
    return HttpResponse("contact")


def speach(request):
    return render(request, 'text_to_speach.html')
