from django.shortcuts import render, render
from django.http import request, HttpResponse, HttpRequest
# Create your views here.
from .models import Entry, User


def HomePage(request) -> object:
    return render(request, "index.html")


def showForm(request):
    return render(request, "form.html")


def Contacts(request):
    return render(request, "contacts.html")
def About(request):
    return render(request,"contacts.html")
def EntryPage(request):
    return render(request,"entries.html")

