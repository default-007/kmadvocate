from django.db import models
from markdownx.models import MarkdownxField
from markdownx.utils import markdownify
from django.shortcuts import reverse


class Service(models.Model):
    name = models.CharField(max_length=30, unique=True)
    icons = models.CharField(max_length=30, blank=True, null=True)
    description = MarkdownxField()

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("website:service", args=[str(self.id)])

    def formatted_markdown(self):
        return markdownify(self.description)

    def body_summary(self):
        return markdownify(self.description[:300] + "...")

    @property
    def imageURL(self):
        try:
            url = self.image.url
        except:
            url = ""
        return url


class Blog(models.Model):
    title = models.CharField(max_length=30)
    author = models.CharField(max_length=30)
    created_at = models.DateTimeField(auto_now_add=True)
    image = models.ImageField()
    text = MarkdownxField()
    quote = MarkdownxField()
    slug = models.SlugField()

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("website:blog", args=[str(self.id)])

    def formatted_markdown(self):
        return markdownify(self.text)
