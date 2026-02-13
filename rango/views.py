from django.shortcuts import render
from django.http import HttpResponse
from rango.models import Category   


def index(request):
    category_list = Category.objects.all()
    context_dict = {'categories': category_list}

    return render(request, 'rango/index.html', context=context_dict)

def about(request):
    return HttpResponse("Rango says here is the about page. <a href='/rango/'>Index</a>")

