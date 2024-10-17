import os
import pandas as pd
import django
from django.conf import settings
from alumini.models import Alumini

# # Set the DJANGO_SETTINGS_MODULE environment variable
# os.environ.setdefault("DJANGO_SETTINGS_MODULE", "core.settings")
# django.setup()

# Path to your CSV file
csv_file_path = "./data.csv"  # Change this to the path of your CSV file

# Read the CSV file into a DataFrame
df = pd.read_csv(csv_file_path)

# Iterate through the DataFrame and create Alumini instances
for index, row in df.iterrows():
    Alumini.objects.create(
        first_name=row["first_name"],
        last_name=row["last_name"],
        email=row["email"],
        full_name=row["full_name"],
        address=row["address"],
        job_title=row["job_title"],
        name_of_business=row["name_of_business"],
        business_address=row["business_address"],
        business_city=row["business_city"],
        business_state=row["business_state"],
        business_zip=row["business_zip"],
        business_phone=row["business_phone"],
        business_email=row["business_email"],
        business_website=row["business_website"],
        business_description=row["business_description"],
        business_category=row["business_category"],
        alumini_discount=row["alumini_discount"] == "True",  # Convert string to boolean
        alumini_discount_description=row["alumini_discount_description"],
        business_logo_link=row["business_logo_link"],
        user_id=row["user_id"],  # You may want to adjust this if using ForeignKey
    )

print("Data inserted successfully.")
