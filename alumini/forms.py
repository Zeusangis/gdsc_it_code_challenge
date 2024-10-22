from django import forms
from .models import AddFromCsv


class AddFromCsvForm(forms.ModelForm):
    class Meta:
        model = AddFromCsv
        fields = ["data"]
