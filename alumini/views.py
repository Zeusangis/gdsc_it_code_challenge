from django.shortcuts import render
from .models import Alumini
from django.contrib.auth.decorators import login_required
from django.db.models import Q
import pandas as pd
from django.http import HttpResponse
import os
from .models import Alumini, Category


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
    categories = Category.objects.all()
    context = {"aluminis": aluminis, "categories": categories}
    return render(request, "alumini/index.html", context)


@login_required(login_url="login")
def account(request):
    return render(request, "alumini/account.html")


@login_required(login_url="login")
def alumni(request, id):

    alumni = Alumini.objects.get(id=id)
    context = {"alumni": alumni}
    return render(request, "alumini/alumni.html", context)


# def add_data(request):
#     # Load the data from the CSV file
#     csv_path = os.path.join(os.path.dirname(__file__), "data.csv")
#     data = pd.read_csv(
#         csv_path
#     )  # Assuming it's a CSV, replace with the correct function if it's a different format.

#     for index, row in data.iterrows():
#         # Fetch or create the category
#         category, created = Category.objects.get_or_create(
#             category=row["business_category"]
#         )

#         # Now create the Alumini entry with the foreign key pointing to the category
#         Alumini.objects.create(
#             first_name=row["first_name"],
#             last_name=row["last_name"],
#             email=row["email"],
#             full_name=row["full_name"],
#             address=row["address"],
#             job_title=row["job_title"],
#             name_of_business=row["name_of_business"],
#             business_address=row["business_address"],
#             business_city=row["business_city"],
#             business_state=row["business_state"],
#             business_zip=row["business_zip"],
#             business_phone=row["business_phone"],
#             business_email=row["business_email"],
#             business_website=row["business_website"],
#             business_description=row["business_description"],
#             business_category=category,  # Foreign key reference
#             alumini_discount=False,
#             alumini_discount_description=row["alumni_discount_description"],
#             business_logo_link=row["business_logo_link"],
#             user_id=row["user_id"],
#         )

#     return HttpResponse("Data added successfully")
