from django.shortcuts import render, redirect
from .models import Alumini
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from .models import Alumini, Category
from django.contrib import messages
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.contrib import auth
import pandas as pd
import os
from django.contrib.auth.decorators import user_passes_test
from .forms import AddFromCsvForm
from django.conf import settings


def error_404_view(request, exception):
    return render(request, "alumini/404.html")


def index(request):
    aluminis = Alumini.objects.select_related("business_category")

    # Handling filtering logic based on search parameters
    if request.method == "GET":
        name = request.GET.get("name", "").strip()
        business = request.GET.get("business_name", "").strip()
        category = request.GET.get("category", "").strip()

        if name or business or category:
            filters = Q()
            if name:
                filters &= Q(full_name__icontains=name)
            if business:
                filters &= Q(name_of_business__icontains=business)
            if category:
                category_obj = Category.objects.get(category=category)
                filters &= Q(business_category=category_obj)

            aluminis = aluminis.filter(filters)

    categories = Category.objects.all()
    page_number = request.GET.get("page", 1)
    paginator = Paginator(aluminis, 12)
    try:
        page_number = int(page_number) if page_number else 1
    except (ValueError, TypeError):
        page_number = 1
    try:
        page_obj = paginator.page(page_number)
    except PageNotAnInteger:
        page_obj = paginator.page(1)
    except EmptyPage:
        page_obj = paginator.page(paginator.num_pages)
    prev_page = int(page_number) - 1 if int(page_number) > 1 else 1
    next_page = (
        int(page_number) + 1
        if int(page_number) < paginator.num_pages
        else paginator.num_pages
    )
    avail_pages = paginator.num_pages > 1
    if not page_obj.object_list:
        no_results = True
    else:
        no_results = False

    context = {
        "paginator": paginator,
        "page_obj": page_obj,
        "prev_page": prev_page,
        "next_page": next_page,
        "avail_pages": avail_pages,
        "no_results": no_results,
        "categories": categories,
    }
    return render(request, "alumini/index.html", context)


@login_required(login_url="login")
def account(request):
    user = request.user
    context = {"user": user}
    return render(request, "alumini/account.html", context)


@login_required(login_url="login")
def alumni(request, id):

    alumni = Alumini.objects.get(id=id)
    context = {"alumni": alumni}
    return render(request, "alumini/alumni.html", context)


@login_required(login_url="login")
def edit_profile(request):
    user = request.user
    if request.method == "POST":
        user.full_name = request.POST.get("name")
        user.phone_number = request.POST.get("phone_number")
        user.address = request.POST.get("address")
        if request.POST.get("password"):
            user.set_password(request.POST.get("password"))
        user.save()
        auth.login(request, user)
        messages.success(request, "Profile updated successfully")
        return redirect("home")
    context = {"user": user}
    return render(request, "alumini/edit_profile.html", context)


# @user_passes_test(lambda u: u.is_superuser)
# def add_data(request):
#     if request.method == "POST":
#         if "csv_file" in request.FILES:
#             print(request.FILES["csv_file"])
#             csv = request.FILES["csv_file"]

#             pd.read_csv(csv)

#         # Process each row in the CSV file and add it to the Alumini table
#         for index, row in csv.iterrows():
#             # Fetch or create the category
#             category, created = Category.objects.get_or_create(
#                 category=row["business_category"]
#             )

#             # Now create the Alumini entry with the foreign key pointing to the category
#             Alumini.objects.create(
#                 first_name=row["first_name"],
#                 last_name=row["last_name"],
#                 email=row["email"],
#                 full_name=row["full_name"],
#                 address=row["address"],
#                 job_title=row["job_title"],
#                 name_of_business=row["name_of_business"],
#                 business_address=row["business_address"],
#                 business_city=row["business_city"],
#                 business_state=row["business_state"],
#                 business_zip=row["business_zip"],
#                 business_phone=row["business_phone"],
#                 business_email=row["business_email"],
#                 business_website=row["business_website"],
#                 business_description=row["business_description"],
#                 business_category=category,  # Foreign key reference
#                 alumini_discount=bool(row["alumini_discount"]),
#                 alumini_discount_description=row["alumni_discount_description"],
#                 business_logo_link=row["business_logo_link"],
#                 user_id=row["user_id"],
#             )

#         return redirect("admin")

#     return render(request, "alumini/upload_csv.html")
