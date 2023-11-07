from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def prem(request):
    return HttpResponse('hii bro')
 
def rajesh(request):
    return HttpResponse('<h1><marquee>I am fine</h1></marquee>')