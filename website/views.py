from django.conf import settings
from django.contrib import messages
from django.shortcuts import redirect
from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from django.views.generic import ListView, DetailView, View, CreateView
from django.http import HttpResponse, HttpResponseRedirect
from .models import *

# Create your views here.
class HomeView(View):
    # common_tags = Post.tags.most_common()[:4]

    def get(self, request):
        services = Service.objects.all()
        blogs = Blog.objects.all()
        template_name = "index.html"
        context = {"services": services, "blogs": blogs}
        return render(request, template_name, context)


class AboutView(View):
    def get(self, request):
        services = Service.objects.all()
        team = Partner.objects.all()
        template_name = "about.html"
        context = {
            "services": services,
            "team": team,
        }
        return render(request, template_name, context)


class ServiceListView(ListView):
    model = Service
    template_name = "service-list.html"


class ServiceView(DetailView):
    model = Service
    template_name = "service-detail.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["service_list"] = Service.objects.all()
        return context


class BlogView(View):
    def get(self, request):
        blogs = Blog.objects.all()
        service_list = Service.objects.all()
        category_list = BlogCategory.objects.all()
        template_name = "blog-page.html"
        context = {
            "blogs": blogs,
            "service_list": service_list,
            "category_list": category_list,
        }
        return render(request, template_name, context)


class BlogDetailView(DetailView):
    model = Blog
    template_name = "blog-single.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["blog_list"] = Blog.objects.all()
        context["service_list"] = Service.objects.all()
        context["category_list"] = BlogCategory.objects.all()
        return context


class TeamView(View):
    def get(self, request):
        teams = Partner.objects.all()
        service_list = Service.objects.all()
        category_list = BlogCategory.objects.all()
        template_name = "team.html"
        context = {
            "teams": teams,
            "service_list": service_list,
            "category_list": category_list,
        }
        return render(request, template_name, context)


class TeamDetailView(DetailView):
    model = Partner
    template_name = "team-single.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["blog_list"] = Blog.objects.all()
        return context


class ContactView(View):
    def get(self, request):
        teams = Partner.objects.all()
        service_list = Service.objects.all()
        category_list = BlogCategory.objects.all()
        template_name = "contact.html"
        context = {
            "teams": teams,
            "service_list": service_list,
            "category_list": category_list,
        }
        return render(request, template_name, context)
