from django.shortcuts import render
from .models import Alumini


def index(request):
    aluminis = Alumini.objects.all()
    context = {"aluminis": aluminis}
    return render(request, "alumini/index.html", context)
