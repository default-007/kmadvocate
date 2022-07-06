from django.conf.urls import include
from django.urls import path
from .views import *
from . import views

app_name = "website"

urlpatterns = [
    path("", HomeView.as_view(), name="home"),
    path("about/", AboutView.as_view(), name="about"),
    path("services/", ServiceListView.as_view(), name="services"),
    path("services/<pk>/", ServiceView.as_view(), name="services"),
    path("blog/", BlogView.as_view(), name="blog"),
    path("blog/<pk>/", BlogDetailView.as_view(), name="blog"),
    path("team/", TeamView.as_view(), name="team"),
    path("team/<pk>/", TeamDetailView.as_view(), name="team"),
    path("contact/", ContactView.as_view(), name="contact"),
]
