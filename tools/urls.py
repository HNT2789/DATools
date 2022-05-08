from django import urls
from django.urls import path

from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("igtools/", views.igtools, name="igtools"),
    path("extools/", views.extools, name="extools"),
    path("cvedes/", views.cvedes, name="cvedes"),
    path("target/", views.burpConvert, name="burpConvert"),
    path("target/exploit=<int:id>", views.exploitsqlmap, name="exploitsqlmap"),
    path("netcraft/", views.netCraft, name="netCraft"),
    path("verbtampering/", views.verbtamper, name="verbtamper"),
    path("subdomain/", views.subdomain, name="subdomain"),
    path("crawler/", views.crawler, name="crawler"),

    # <str:filepath>/
]
