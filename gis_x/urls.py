from django.urls import path

from . import views

urlpatterns = [
    path("", views.gis_x, name="gis_x"),

]