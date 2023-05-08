# http://127.0.0.1:8000/
from django.http import HttpResponse
from django.shortcuts import render
from django.shortcuts import redirect


def index(request):
    return render(request, 'index.html')


def analyze(request):
    # Get the text
    djtext = request.POST.get('text', 'default')

    # Check checkbox values
    removepunc = request.POST.get('removepunc', 'off')
    fullcaps = request.POST.get('fullcaps', 'off')
    newlineremover = request.POST.get('newlineremover', 'off')
    extraspaceremover = request.POST.get('extraspaceremover', 'off')
    numberremover = request.POST.get('numberremover', 'off')

    # Check which checkbox is on
    if removepunc == "on":
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        analyzed = ""
        for char in djtext:
            if char not in punctuations:
                analyzed = analyzed + char

        params = {'purpose': 'Removed Punctuations', 'analyzed_text': analyzed}
        djtext = analyzed

    if (fullcaps == "on"):
        analyzed = ""
        for char in djtext:
            analyzed = analyzed + char.upper()

        params = {'purpose': 'Changed to Uppercase', 'analyzed_text': analyzed}
        djtext = analyzed

    if (extraspaceremover == "on"):
        analyzed = ""
        for index, char in enumerate(djtext):
            # It is for if a extraspace is in the last of the string
            if char == djtext[-1]:
                if not (djtext[index] == " "):
                    analyzed = analyzed + char

            elif not (djtext[index] == " " and djtext[index + 1] == " "):
                analyzed = analyzed + char

        params = {'purpose': 'Removed NewLines', 'analyzed_text': analyzed}
        djtext = analyzed

    if (newlineremover == "on"):
        analyzed = ""
        for char in djtext:
            if char != "\n" and char != "\r":
                analyzed = analyzed + char

        params = {'purpose': 'Removed NewLines', 'analyzed_text': analyzed}

    if (numberremover == "on"):
        analyzed = ""
        numbers = '0123456789'

        for char in djtext:
            if char not in numbers:
                analyzed = analyzed + char

        params = {'purpose': 'Removed NewLines', 'analyzed_text': analyzed}
        djtext = analyzed

    if (
            removepunc != "on" and newlineremover != "on" and extraspaceremover != "on" and fullcaps != "on" and numberremover != "on"):
        return HttpResponse("please select any operation and try again")

    return render(request, 'analyze.html', params)


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
