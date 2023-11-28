from django.http import HttpResponse
from django.shortcuts import render


def get_greetings(request):
    return HttpResponse('<h1>Denis Zhurid</h1>')
