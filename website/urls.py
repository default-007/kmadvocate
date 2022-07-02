from django.conf.urls import include
from django.urls import path
from .views import *
from . import views

app_name = "website"

urlpatterns = [
    path("", HomeView.as_view(), name="home"),
    # path("about/", AboutView.as_view(), name="about"),
]
