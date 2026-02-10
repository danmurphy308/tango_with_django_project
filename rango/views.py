from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return render(request, 'rango/index.html')

def about(request):
    return HttpResponse("Rango says here is the about page. <a href='/rango/'>Index</a>")
