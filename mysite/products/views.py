from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello World")

def new(request):
    return HttpResponse("New products! Just in today!")