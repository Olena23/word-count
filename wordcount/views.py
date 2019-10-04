from django.http import HttpResponse
from django.shortcuts import render


def home(request):
    return HttpResponse(render(request, 'home.html'))


def count(request):
    fulltext = request.GET['fulltext']
    number_of_words = len(fulltext.split())
    word_frequency = {}
    for word in fulltext.split():
        word_frequency[word] = fulltext.split().count(word)
    return HttpResponse(render(request, 'count.html', {'fulltext': fulltext, 'number_of_words': number_of_words,
                                                       'word_frequency': word_frequency}))
