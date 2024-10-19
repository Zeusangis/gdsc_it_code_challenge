import pandas as pd
import os
from django.shortcuts import render
from .models import Alumini
from django.http import HttpResponse
from django.conf import settings


def index(request):
    aluminis = Alumini.objects.all()
    if request.method == "POST":
        query = request.POST.get("search")
        aluminis = Alumini.objects.filter(full_name__icontains=query)
    context = {"aluminis": aluminis}
    return render(request, "alumini/index.html", context)


def account(request):
    return render(request, "alumini/account.html")


def alumni(request, id):
    alumni = Alumini.objects.get(id=id)
    context = {"alumni": alumni}
    return render(request, "alumini/alumni.html", context)
