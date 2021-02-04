from django.shortcuts import render
from django.http import HttpResponse

def index(response):
    return HttpResponse("Yeah this guy is working good but in dev branch")
