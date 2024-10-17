import pandas as pd
import os
from django.shortcuts import render
from .models import Alumini
from django.http import HttpResponse
from django.conf import settings


def index(request):
    aluminis = Alumini.objects.all()
    context = {"aluminis": aluminis}
    return render(request, "alumini/index.html", context)
