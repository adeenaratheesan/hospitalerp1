from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def duty(request):
    return HttpResponse('nurse home screen')
