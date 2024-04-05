from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.contrib.auth import authenticate, login

def index(request):
    template = loader.get_template("HealthTracker/index.html")
    context = {}
    return HttpResponse(template.render(context, request))

def about(request):
    return render(request, 'HealthTracker/about.html')