from django.urls import path
from .views import *

urlpatterns = [
    path("", index, name="home"),
    path("account/", account, name="account"),
    path("alumni/<str:id>/", alumni, name="alumni"),
    path("edit_profile/", edit_profile, name="edit_profile"),
    # path("add_data/", add_data, name="add_data"),
]
handler404 = "alumini.views.error_404_view"
