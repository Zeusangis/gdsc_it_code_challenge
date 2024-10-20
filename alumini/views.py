from django.shortcuts import render
from .models import Alumini
from users.models import CustomUser as User


def index(request):
    aluminis = Alumini.objects.values(
        "id", "full_name", "job_title", "name_of_business", "business_category"
    )
    if request.method == "POST":
        query = request.POST.get("search")
        aluminis = Alumini.objects.values(
            "id", "full_name", "name_of_business", "business_category"
        ).filter(full_name__icontains=query)
    context = {"aluminis": aluminis}
    return render(request, "alumini/index.html", context)


def account(request):
    return render(request, "alumini/account.html")


def alumni(request, id):
    alumni = Alumini.objects.get(id=id)
    context = {"alumni": alumni}
    return render(request, "alumini/alumni.html", context)
