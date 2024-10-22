from django.db import models
import shortuuid
from django.utils.translation import gettext_lazy as _
from django.core.validators import FileExtensionValidator


class Alumini(models.Model):
    id = models.CharField(
        _("ID"), primary_key=True, max_length=22, default=shortuuid.uuid, editable=False
    )
    first_name = models.CharField(_("First Name"), max_length=100)
    last_name = models.CharField(_("Last Name"), max_length=100)
    email = models.EmailField(_("Email Address"), unique=True)
    full_name = models.CharField(_("Full Name"), max_length=100)
    address = models.CharField(_("Address"), max_length=100)
    job_title = models.CharField(_("Job Title"), max_length=100)
    name_of_business = models.CharField(_("Name of Business"), max_length=100)
    business_address = models.CharField(_("Business Address"), max_length=100)
    business_city = models.CharField(_("Business City"), max_length=100)
    business_state = models.CharField(_("Business State"), max_length=100)
    business_zip = models.CharField(_("Business Zip"), max_length=100)
    business_phone = models.CharField(_("Business Phone"), max_length=100)
    business_email = models.EmailField(_("Business Email"), unique=True)
    business_website = models.CharField(_("Business Website"), max_length=100)
    business_description = models.TextField(_("Business Description"), max_length=100)
    business_category = models.ForeignKey(
        "Category", verbose_name=_("Business Category"), on_delete=models.CASCADE
    )
    alumini_discount = models.BooleanField(_("Alumini Discount"), default=False)
    alumini_discount_description = models.TextField(
        _("Alumini Discount Description"), max_length=100, blank=True, null=True
    )
    business_logo_link = models.CharField(_("Business Logo Link"), max_length=100)
    user_id = models.CharField(_("User ID"), max_length=100)
    created_at = models.DateTimeField(_("Created At"), auto_now_add=True)

    def __str__(self):
        return self.full_name


class AddFromCsv(models.Model):
    id = models.CharField(
        _("ID"), primary_key=True, max_length=22, default=shortuuid.uuid, editable=False
    )
    data = models.FileField(
        _("CSV File"),
        upload_to="csv_files/",
        validators=[FileExtensionValidator(["csv"])],
    )

    def __str__(self):
        return self.id


class Category(models.Model):
    id = models.CharField(
        _("ID"), primary_key=True, max_length=22, default=shortuuid.uuid, editable=False
    )
    category = models.CharField(_("Category"), max_length=100)
    created_at = models.DateTimeField(_("Created At"), auto_now_add=True)

    def __str__(self):
        return self.category

    class Meta:
        verbose_name_plural = "Categories"
