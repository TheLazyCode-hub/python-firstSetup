from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def index(request):
    #    return HttpResponse("Welcome to home page")
    return render(request, 'index.html')


def about(request):
    # return HttpResponse("Welcome to About page")
    return render(request, "about.html")


def contact(request):
    # return HttpResponse("Welcome to contact page")
    return render(request, "contact.html")
