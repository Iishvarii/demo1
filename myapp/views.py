from django.shortcuts import render

from django.http import HttpResponse

def bweb(request):
    return HttpResponse("Hello, world!")