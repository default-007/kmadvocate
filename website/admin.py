from unicodedata import category
from django.contrib import admin
from django.contrib.auth.models import Group
from markdownx.admin import MarkdownxModelAdmin
from .models import *

admin.site.unregister(Group)

# Register your models here.
@admin.register(Service)
class ServiceAdmin(MarkdownxModelAdmin):
    list_display = ("name", "created_date")
    list_filter = ("created_date",)
    search_fields = ("name",)


admin.site.register(BlogCategory)


@admin.register(Blog)
class BlogPostAdmin(MarkdownxModelAdmin):
    list_display = ("title", "created_at", "author")
    list_filter = ("created_at",)
    search_fields = ("title",)


@admin.register(Partner)
class PartnerAdmin(MarkdownxModelAdmin):
    list_display = ("names", "position", "email")
    list_filter = ("position",)
    search_fields = ("names",)
