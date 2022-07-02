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
