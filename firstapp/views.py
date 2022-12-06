from django.shortcuts import render
from django.http import HttpResponse
from firstapp.models import Contact
from datetime import datetime

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
    if request.method == "POST":
        name = request.POST.get('name') + ' ' + request.POST.get('surname')
        phone = request.POST.get('phone')
        email = request.POST.get('email')
        msg = request.POST.get('message')
        print(name + ' ' + phone + ' ' + email + ' ' + msg)
        contact = Contact(name=name, phone=phone, email=email,
                          msg=msg, date=datetime.now())
        contact.save()
    return render(request, "contact.html", context)
