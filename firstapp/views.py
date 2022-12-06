from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def index(request):
    #    return HttpResponse("Welcome to home page")
    context = {
        "name": "Gaurav",
        "title": "Index"
    }
    return render(request, 'index.html', context)


def about(request):
    # return HttpResponse("Welcome to About page")
    context = {
        "title": "About"
    }
    return render(request, "about.html", context)


def contact(request):
    # return HttpResponse("Welcome to contact page")
    context = {
        "title": "Contact"
    }
    return render(request, "contact.html", context)
