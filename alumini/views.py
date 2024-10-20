from django.shortcuts import render
from .models import Alumini
from django.contrib.auth.decorators import login_required
from django.db.models import Q


@login_required(login_url="login")
def index(request):
    aluminis = Alumini.objects.values(
        "id", "full_name", "job_title", "name_of_business", "business_category"
    )

    if request.method == "POST":
        name = request.POST.get("name", "").strip()
        business = request.POST.get("business_name", "").strip()

        if name or business:
            filters = Q()
            if name:
                filters &= Q(full_name__icontains=name)
            if business:
                filters &= Q(name_of_business__icontains=business)

            aluminis = Alumini.objects.values(
                "id", "full_name", "job_title", "name_of_business", "business_category"
            ).filter(filters)

    context = {"aluminis": aluminis}
    return render(request, "alumini/index.html", context)


@login_required(login_url="login")
def account(request):
    return render(request, "alumini/account.html")


@login_required(login_url="login")
def alumni(request, id):
    alumni = Alumini.objects.get(id=id)
    context = {"alumni": alumni}
    return render(request, "alumini/alumni.html", context)
