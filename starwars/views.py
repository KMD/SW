from django.shortcuts import render

from django.http import HttpResponse


def index(request):
    return render(request, 'starwars/collections.html', {})

def collection(request, size):
    return render(request, 'starwars/collection.html', {})
