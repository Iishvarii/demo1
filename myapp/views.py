from django.shortcuts import render

from django.http import HttpResponse

def bweb(request):
    return HttpResponse("Hello, this is bweb view 完成")