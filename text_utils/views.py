# http://127.0.0.1:8000/
from django.http import HttpResponse
from django.shortcuts import render
from django.shortcuts import redirect


def index(request):
    return render(request, 'index.html')


def removepunc(request):
    djtext = request.GET.get('text', 'default')
    print(djtext)
    return HttpResponse("remove punc")


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
