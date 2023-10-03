from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("about", views.about, name="about"),
    path("analyspojv", views.analyspojv, name="analyspojv"),
    path("analysudob", views.analysudob, name="analysudob"),
    path("analyswater", views.analyswater, name="analyswater"),
    path("analyskorm", views.analyskorm, name="analyskorm"),
    path("gis", views.gis, name="gis"),
    path("securityplant", views.securityplant, name="securityplant"),
]